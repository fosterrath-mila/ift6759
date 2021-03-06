# Utility modules

You will have to write many functions during this project that may contain common and reusable
code snippets. Such snippets (once properly tested!) are always nice to keep around in some
kind of 'utility' module. We decided to provide a handful of such useful functions that
may help you develop visualization and debugging tools faster. Some of them might also be 
necessary should you decide to create your own data packaging strategy based on HDF5 or
compressed images. You can find them [here](utils.py).

Some of the noteworthy utility functions are detailed below. You should always consider these
functions as "potentially buggy" unless you understand them and have tested them yourself.
Feel free to modify and add functions to the ``utils.py`` module as you wish. Finally, make
sure you install the proper dependencies (e.g. OpenCV, matplotlib) before using them.

## Compressing and decompressing numpy arrays

Your data loading strategy might require you to extract and repackage useful arrays from the
NetCDF or HDF5 files we provide in order to save disk space and/or speed up processing. If
you use our HDF5 files, you will have to manually decompress the information stored in them
first. If you want to create new HDF5 files, you might have to compress your own data as well.

For compression, we provide a simple utility function (``compress_array``) that converts
numpy arrays into byte strings that can be stored in dynamic-length HDF5 datasets. For
decompression, we provide the opposite operation (``decompress_array``) which will convert
the byte string back into a numpy array. In both cases, depending on the encoding used,
you might have to import various 3rd-party dependencies into your code (e.g. OpenCV, LZ4).

Example usage:
```
>>> array = np.random.randint(255, size=(300, 300)).astype(np.uint8)
>>> array  # since this is a 2D 8-bit array, default auto compression will use JPEG
array([[231,   5,  46, ...,  55,  92,  71],
       ...,
       [217, 140, 204, ...,  19, 184, 151]], dtype=uint8)
>>> code = utils.compress_array(array, compr_type="auto")
>>> code[0:30]  # this will show the beginning of the JPEG header...
b'uint8+jpg\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x01,\x01,\x00\x00\xff'
>>> len(code)  # should be smaller than 300x300 = 90000, i.e. the original size
77420
>>> decoded_array = utils.decompress_array(code, dtype=np.uint8, shape=(300, 300))
>>> decoded_array  # since it used JPEG, there might be some information loss
array([[231,   4,  46, ...,  54,  91,  71],
       ...,
       [218, 142, 202, ...,  21, 183, 146]], dtype=uint8)
```

## Reading numpy arrays from HDF5 files

The HDF5 archives we provide contain compressed numpy arrays as detailed [here](datasources.md).
To properly reload these arrays, we provide a utility function (``fetch_hdf5_sample``)
that can be used on an already-opened HDF5 archive. This function will call the
``decompress_array`` utility detailed above as necessary. The "sample index" argument
given to ``fetch_hdf5_sample`` corresponds to the offset encoded into the metadata dataframes
described [here](dataframe.md).

Example usage:
```
>>> hdf5_path = "/project/cq-training-1/project1/data/hdf5v7_8bit/2010.06.01.0800.h5"
>>> hdf5_offset = 32  # this would correspond to: 2010.06.01.0800 + (32)*15min = 2010.06.01.1600
>>> with h5py.File(hdf5_path, "r") as h5_data:
>>>   ch1_data = utils.fetch_hdf5_sample("ch1", h5_data, hdf5_offset)
>>> ch1_data.shape  # channel data is saved as 2D array (HxW)
(650, 1500)
>>> ch1_data  # the utility function will automatically reconvert the data to float32
array([[-1.0784250e-04, -1.0784250e-04, -1.0784250e-04, ...,
         3.7579414e-01,  3.4611768e-01,  3.6590198e-01],
       ...,
       [ 4.9450004e-01,  4.7471571e-01,  4.9450004e-01, ...,
         7.3191184e-01,  7.8137261e-01,  8.2094121e-01]], dtype=float32)
```

## Visualizing the content of an HDF5 file

Both 8-bit and 16-bit HDF5 archives can be visualized using the provided ``viz_hdf5_imagery``
function. This may help you understand the role of each available imagery channel and the
impact of cloud cover over a measurement station.

The animation shown in the project presentation is obtained using this function with 8-bit
imagery for June 21st, 2010, and for the following channels: ``["ch1", "ch2", "ch3", "ch4", "ch6"]``.

Remember that you might not be able to forward display windows from Helios nodes to your
local display manager. This might force you to run these visualization completely offline.

Example usage:
```
>>> hdf5_path = "/some/local/path/project1/data/hdf5v7_8bit2010.06.21.0800.h5"
>>> target_channels = ["ch1", "ch2", "ch3", "ch4", "ch6"]
>>> dataframe_path = "/some/local/path/project1/data/some.local.catalog.pkl"
>>> stations = {"BND": (lat, lon, elev), "TBL": (lat, lon, elev), ...}
>>> viz_hdf5_imagery(hdf5_path, target_channels, dataframe_path, stations)
# the above line will block until the visualization is stopped...
```

## Visualizing GHI predictions

Finally, we provide a function to display GHI plots (measured values, clearsky estimates,
and predicted values) for a set of stations over different time horizons: ``viz_predictions``.
In this case, the function expects to receive the text file generated by the evaluation
script ([described here](evaluation.md)) which contains your model's raw predictions for a
set of timestamps. These timestamps must also be provided through the test configuration file,
for which you also have an example [here](dummy_test_cfg.json).

Feel free to ignore this function and instead only rely on its subfunctions (``draw_daily_ghi``
and ``plot_ghi_curves``) if you want to incorporate it into your own code, or if you wish
to customize it in any way.

Remember that you might not be able to forward display windows from Helios nodes to your
local display manager. This might force you to run these visualization completely offline.
