# Data Sources

The raw NetCDF imagery of the Geostationary Operational Environmental Satellite (GOES) provided by the
NOAA over the period of interest is quite voluminous (**over 800 GBs**). It is split into 15-minute chunks,
and the imagery itself covers all of the continental United States with several 16-bit channels. For this
project's goals, we only need to focus on small areas of interest around the GHI measurement stations.
Furthermore, many time periods are not very useful for GHI prediction (for example, night time).
It is thus recommended to preprocess this data in order to extract only the useful bits and speed up
training. Remember: faster data loading means more efficient training, and more efficient training means
more time to evaluate models and tune hyperparameters.

As mentionned in the [disk usage documentation](https://github.com/mila-iqia/ift6759/tree/master/disk-usage.md),
the data for this project is available in a shared read-only directory:
```
/project/cq-training-1/project1/data
```

We provide three versions of the GOES imagery in order to help you start the project:
 - The original, 16-bit, GZip-compressed (lossless) NetCDF (.nc) files, in 15-minute chunks.
 - Repackaged, 16-bit, JPEG2000-compressed (lossy) HDF5 (.h5) archives, in 1-day chunks.
 - Repackaged, 8-bit, JPEG-compressed (lossy) HDF5 (.h5) archives, in 45-day chunks.

The easiest way to associate a UTC timestamp with a specific imagery source is to rely on the provided
[dataframe](https://github.com/mila-iqia/ift6759/blob/master/projects/project1/dataframe.md).

## Original NetCDF files

You might not be able to properly store, copy or duplicate the original data due to storage limitations on
Helios. Furthermore, multiple users simultaneously accessing small files on the cluster can drastically reduce
I/O throughput. However, since it is untouched and in its original format, you can use the NetCDF metadata and
extra channels as you please. Understanding the NetCDF file contents might also be necessary in order to work
with the other versions of the data.

Besides, note that the channel data is compressed inside the NetCDF files themselves (GZip), and it will be
automatically decompressed when the file is opened. If you only want to crop a small region around a station,
loading and decompressing the data for the entire continental US for each training iteration might create a
dramatic ingestion overhead in your training process.

You can use [``netCDF4``](https://unidata.github.io/netcdf4-python/netCDF4/index.html) or
[``h5netcdf``](https://github.com/shoyer/h5netcdf) to read NetCDF files in Python. The latter is less documented
but will it allow multithreaded read access to .nc files "out-of-the-box".

## 16-bit HDF5 archives

The 16-bit, JPEG2000-compressed HDF5 archives require roughly 50% less storage space than the original
NetCDF files, and incur a maximum loss of less than ~1% over the original channel's value range. HDF5 archives
also allow small chunks of data to be read and decompressed individually. This combination provides a good tradeoff
between storage cost and data loss. However, JPEG2000 decompression may be much slower than GZip or JPEG
decompression. It will be up to you to determine which solution is best.

Utility functions for unpacking the compressed data arrays are provided in this repository. These functions are
based on [OpenCV](https://opencv.org/), but you could easily modify them to use any other image reading library.
HDF5 files can be easily opened using [``h5py``](https://www.h5py.org/).

## 8-bit HDF5 archives

The 8-bit, JPEG-compressed HDF5 archives require nearly 85% less storage space than the original GZipped
NetCDF files. However, this pre-quantified JPEG compression is much more lossy than the other two alternatives,
as encoded values can fluctuate by up to 100% of their original range in the worst cases (i.e. in dark
channels). However, interestingly, this is not easily visible to the naked eye, and the imagery still looks
intact when inspected. You will have to determine whether these small perturbations can negatively affect the
behavior of your model, and whether the convenience of the extreme compression counterbalances this potential impact.

Once again, utility functions for unpacking the compressed data arrays are provided in this repository. These
functions are based on [OpenCV](https://opencv.org/), but you could easily modify them to use any other
image reading library. Curious students are also encouraged to dig in and see exactly what information is lost
in the compression process...
