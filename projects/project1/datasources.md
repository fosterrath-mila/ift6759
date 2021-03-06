# Data Sources

The raw NetCDF imagery of the Geostationary Operational Environmental Satellite (GOES)-13 provided by the
NOAA over the period of interest is quite voluminous (**over 800 GBs**). It is split into 15-minute chunks,
and the imagery itself covers all of the continental United States with several 16-bit channels. For this
project's goals, you might only need to focus on small areas of interest (i.e. patches) around the GHI
measurement (SURFRAD) stations. Furthermore, many time periods are not very useful for GHI prediction (for
example, night time values are not considered in the evaluation of the models). It is thus recommended to
preprocess this data in order to extract only the useful bits and speed up training. Remember: faster data
loading means more efficient training, and more efficient training means more time to try models and tune
hyperparameters.

As mentionned in the [disk usage documentation](../../disk-usage.md), the data for this project is available
in a shared read-only directory:
```
/project/cq-training-1/project1/data
```

We provide three versions of the GOES imagery in order to help you start the project:
 - The original, 16-bit, GZip-compressed (lossless) NetCDF (.nc) files, in 15-minute chunks.
 - Repackaged, 16-bit, JPEG2000-compressed (lossy) HDF5 (.h5) archives, in 1-day chunks.
 - Repackaged, 8-bit, JPEG-compressed (lossy) HDF5 (.h5) archives, in 1-day chunks.

We provide only a little bit of documentation for the content of these data sources below. For the NetCDF
data, you might be able to find more GOES-13 documentation online, but manual inspection using Python should be
sufficient to identify what to extract. For the HDF5 archives, opening them manually and using the utility
functions described [here](utilities.md) should be enough to get you started. Remember, real-world data is
rarely well-documented: you will almost always have to dig in and try to understand the structure on your own.
This is no different, and it should provide you a good opportunity to learn how to use debugging/inspection tools.

Finally, note that the easiest way to associate a UTC timestamp with the provided imagery sources is to rely on
the provided [dataframe](dataframe.md).

## Original NetCDF files

You might not be able to properly store, copy or duplicate the original NetCDF data due to storage limitations
on Helios. Furthermore, multiple users simultaneously accessing small files on the cluster can drastically
reduce I/O throughput. However, since it is untouched and in its original format, you can use the metadata of
the attributes and channels as you please.

Understanding the NetCDF file contents might be necessary in order to properly extract the channel arrays
without introducing (or carrying over) invalid values. We recommend that you look at the conventions for
the packaging of [Climate and Forecast Metadata](http://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/build/ch08.html),
especially the sections regarding the use of scaling factors and missing/filled values. Those working with the
HDF5 data will have less options in terms of how they wish to handle missing/corrupted array values.

Besides, note that the channel data is compressed inside the NetCDF files themselves (GZip), and it will be
automatically decompressed when the file is opened by the Python package you are using. If you only want to
crop a small region around a station, loading and decompressing the data for the entire continental US in each
training minibatch might create a dramatic ingestion overhead. This is where cropping becomes useful...

You can use [``netCDF4``](https://unidata.github.io/netcdf4-python/netCDF4/index.html) or
[``h5netcdf``](https://github.com/shoyer/h5netcdf) to read NetCDF files in Python. The latter is less documented
but will it allow multithreaded read access to .nc files "out-of-the-box" with fewer issues.

## Decompressing HDF5 data

Utility functions for unpacking the compressed data arrays in the HDF5 files are provided [here](utilities.md).
These functions are based on [``OpenCV``](https://opencv.org/), but you could easily modify them to use any other
image reading library. HDF5 files can be easily opened using [``h5py``](https://www.h5py.org/).

The HDF5 archives contain the primary channels of interest extracted from the NetCDF files as well as the latitude
and longitude maps used to associate array values to geographic locations. Each of these is encoded into a dataset
object that supports seeking in order to reload one array at a time (i.e. at one timestamp). You should look at the
``fetch_hdf5_sample`` function of the utility module in order to reload an array. If you plan on repackaging your
own HDF5 files, feel free to use the same archive structure (and utility function), or devise your own.

For an overview of the HDF5 file format & specification, see [this introduction](https://support.hdfgroup.org/HDF5/Tutor/HDF5Intro.pdf).

Curious students are also encouraged to dig in and see exactly what information is lost in the compression process,
as what you learn might help you decide which data source to rely on...

### 16-bit HDF5 archives

The 16-bit, JPEG2000-compressed HDF5 archives require roughly 50% less storage space than the original
NetCDF files, and incur a maximum loss of less than ~1% over the original channel's value range. HDF5 archives
also allow small chunks of data to be read and decompressed individually. This combination provides a good tradeoff
between storage cost and data loss. However, JPEG2000 decompression is much slower than GZip or JPEG
decompression. It will be up to you to determine the impact of the various tradeoffs.

### 8-bit HDF5 archives

The 8-bit, JPEG-compressed HDF5 archives require nearly 85% less storage space than the original GZipped
NetCDF files. However, this pre-quantified JPEG compression is much more lossy than the other two alternatives,
as encoded values can fluctuate by up to 60% of their original range in the worst cases (i.e. in dark
regions). However, interestingly, this is not easily visible to the naked eye, and the imagery still looks
intact when visualized. You will have to determine whether these small perturbations can negatively affect the
behavior of your model, and whether the convenience of the extreme compression counterbalances this potential impact.

## Building an efficient data loading pipeline

See [this link](https://www.tensorflow.org/guide/data_performance) for a fairly in-depth tutorial on the development
and optimization of ``tf.data`` pipelines. We recommend focusing on efficient data loaders at an early point in
the project as it can become a serious bottleneck later on.

For optimal cluster I/O performance, it is recommended to store data in files that are at least 100MB, and inside
SLURM's temporary directory (``$SLURM_TMPDIR``).

### Pipeline formatting

We expect your data loading pipeline to be a ``tf.data.Dataset`` object (or have a compatible object interface).
Each iteration over this object should produce a tuple. Each tuple's last-position element should be a tensor
of target GHI values. All other tuple elements should be provided as inputs for your model. A simple pipeline
implementation will return two-element tuples, i.e. an input tensor for your model and the target GHI value tensor
it should predict. An unpacking strategy for the tuples produced by a pipeline is illustrated below:
```
data_loader = some.module.create_data_loader(...)
model = some.other.module.create_model(...)
...
# code below runs a single epoch
for (input_a, input_b, ..., target_output) in data_loader:
    with tf.GradientTape() as tape:
        predictions = model(input_a, input_b, ...)
        loss = criterion(y_true=target_output, y_pred=predictions)
    grads = tape.gradient(...)
    ...
...
```

Respecting this expected format will be important in order to make your data loading pipeline compatible with
our [evaluation script](evaluation.md). In that case, you will have to reinstantiate your pipeline to load the
(withheld) test data. This test data will **NOT** include the ground truth GHI values, meaning you will have
to either return zero-filled target output tensors, or simply return ``None`` as the last element of the
generated tuples. While this approach may seem strange to some, we argue that it is better than writing two
versions of your data loading pipeline and introducing new potential disparities.
