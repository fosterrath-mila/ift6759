# Metadata Catalog (Dataframe)

We provide a metadata catalog as a [Pandas dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
to simplify the indexing of raw GHI values and imagery data for training and evaluation purposes. Your
data loading pipeline is expected to scan this dataframe in order to know which sequences it should load.
A similar dataframe (minus several GT-related columns) will be used for the final evaluation of your
submitted model's performance ([click here](https://github.com/mila-iqia/ift6759/blob/master/projects/project1/evaluation.md)
for more information).

The pickle file used to reinstantiate the Pandas dataframe is located in the shared (read-only) directory
mentionned in the [disk usage documentation](https://github.com/mila-iqia/ift6759/tree/master/disk-usage.md),
that is:
```
/project/cq-training-1/project1/data
```

The dataframe is indexed using timestamps compatible with Python's ``datetime`` package ([more
info here](https://docs.python.org/3/library/datetime.html)). These timestamps are in Coordinated
Universal Time (or "UTC"), so do not be worried if sunrise/sunset times seem off. Just keep
this in mind if you plan on using local (station) times in your solution. The dataframe possesses
an entry for each 15 minute interval over the entire period it covers. If data is missing in that
interval, the dataframe will still have an entry, but some of its attributes may be "NaNs".

## Dataframe columns

Each column in the dataframe specifies an attribute for every 15-minute entry. Details on these attributes
are provided below:

 - ``ncdf_path``: The absolute path (on Helios) to the NetCDF file containing the raw (16-bit) imagery data
   for the specified 15-minute interval. Can be "nan" if unavailable. Reminder: the raw NetCDF files are
   only ~4MB chunks, and simultaneous I/O operations on these might become very slow on the cluster.
 - ``hdf5_path``: The absolute path (on Helios) to the HDF5 archive containing a compressed version (8-bit
   or 16-bit) of the imagery data for the specified 15-minute interval. Since this archive will likely
   be an aggregate of many 15-minute chunks, the offset below must be used to locate the proper timestamp.
 - ``hdf5_offset``: An integer, non-negative offset value used to index the 15-minute data timestamp that 
   corresponds to this entry in the previously specified HDF5 archive.
 - ``<station_code>_DAYTIME``: a binary flag (0/1) indicating whether it is day time at the station or not.
 - ``<station_code>_CLOUDINESS``: a categorical flag (night/cloudy/slightly cloudy/clear/variable) indicating
   the weather conditions at the station. This is a rough estimate based on a heuristic, and may be useful
   to analyze the performance of your model in various conditions. This value will not be available in the
   dataframe used for the final test.
 - ``<station_code>_CLEARSKY_GHI``: the GHI estimation at the station obtained using the "clear sky" model.
   This value will not be available in the dataframe used for the final test.
 - ``<station_code>_GHI``: the real (measured) GHI at the station. This is the "ground truth" that your
   model should predict, and it will obviously not be available in the dataframe used for the final test.

For more information on the NetCDF and HDF5 files, see
[this page](https://github.com/mila-iqia/ift6759/blob/master/projects/project1/datasources.md).
