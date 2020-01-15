# Metadata Catalog (Dataframe)

We provide a metadata catalog as a [Pandas dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
to simplify the indexing of raw GHI values and imagery data for training and evaluation purposes. Your
data loading pipeline is expected to scan this dataframe in order to know which data it should load.
A similar dataframe (minus several GT-related columns) will be used for the final evaluation of your
submitted model's performance ([see this page](evaluation.md) for more information).

The pickle file used to reinstantiate the Pandas dataframe is located in the shared (read-only) directory
mentionned in the [disk usage documentation](../../disk-usage.md), that is:
```
/project/cq-training-1/project1/data/catalog.helios.public.20100101-20160101.pkl
```

The dataframe is indexed using timestamps compatible with Python's ``datetime`` package ([more
info here](https://docs.python.org/3/library/datetime.html)). These timestamps are in Coordinated
Universal Time (or "UTC"), so do not be worried if sunrise/sunset times seem off. Just keep
this in mind if you plan on using local (station) times in your solution. The dataframe possesses
an entry for every 15 minute interval over the entire 2010-2015 period. If data is missing in an
interval, the dataframe will still have an indexed entry, but some of its attributes may be "NaNs".

## Dataframe columns

Each column in the dataframe specifies an attribute for every 15-minute entry. Details on these attributes
are provided below:

 - ``ncdf_path``: The absolute path (on Helios) to the NetCDF file containing the raw (16-bit) imagery data
   for the specified 15-minute interval. Can be "nan" if unavailable. Reminder: the raw NetCDF files are
   only ~4MB chunks, and simultaneous I/O operations on these might become very slow on the cluster.
 - ``hdf5_<x>bit_path``: The absolute path (on Helios) to an HDF5 archive containing a compressed version
   (8-bit or 16-bit) of the imagery data for the specified 15-minute interval. Since this archive will likely
   be an aggregate of many 15-minute entries, the offset below must be used to locate the proper entry.
 - ``hdf5_<x>bit_offset``: An offset (non-negative integer) value used to point to the correct 15-minute
   data slice in an HDF5 archive that corresponds to this row's timestamp.
 - ``<station_code>_DAYTIME``: a binary flag (0/1) indicating whether it is day time at the station or not.
 - ``<station_code>_CLOUDINESS``: a categorical flag (night/cloudy/slightly cloudy/clear/variable) indicating
   the weather conditions at the station. This is a rough estimate based on a heuristic, and may be useful
   to analyze the performance of your model in various conditions. This value will not be available in the
   dataframe used for the final test.
 - ``<station_code>_CLEARSKY_GHI``: the GHI estimation at the station obtained using the "clear sky" model.
   See the section below for more information on the model used.
 - ``<station_code>_GHI``: the real (measured) GHI at the station. This is the "ground truth" that your
   model should predict, and it will obviously not be available in the dataframe used for the final test.
   Remember: this value is unavailable ("NaN") at at regular intervals (roughly every three hours starting
   at mightnight every day), but it might also be missing at other random timestamps.

For more information on the NetCDF and HDF5 files, see [this page](datasources.md).

## SURFRAD Stations

We are targeting seven stations of interest located in continental United States. Their coordinates
(latitude, longitude, elevation) are provided below. The station acronyms can be used to lookup the
columns related to that particular station in the catalog.

 - Bondville, IL ("BND") @ 40.05192, -88.37309, 230m;
 - Table Mountain, CO ("TBL") @ 40.12498, -105.23680, 1689m;
 - Desert Rock, NV ("DRA") @ 36.62373, -116.01947, 1007m;
 - Fort Peck, MT ("FPK") @ 48.30783, -105.10170, 634m;
 - Goodwin Creek, MS ("GWN") @ 34.25470, -89.87290, 98m;
 - Penn. State University, PA ("PSU") @ 40.72012, -77.93085, 376m;
 - Sioux Falls, SD ("SXF") @ 43.73403, -96.62328, 473m.

You will need the latitude/longitude coordinates above to locate the stations within the pixelized
arrays of the NetCDF/HDF5 files. These files contain the 1D arrays required to map these coordinate to
pixel offset values directly.

Finally, note that the final evaluation will use these same stations. Your report should nonetheless contain
a brief discussion of how well you would expect your model would perform if it was applied to other regions.

## Cloudiness flag

The cloudiness flag given in the dataframe is inspired by the work of Tina et al. (2012), "Analysis of
forecast errors for irradiance on the horizontal plane" (doi:10.1016/j.enconman.2012.05.031). The PDF of this
paper is available [in the repository](tina2012.pdf). The cloudiness flag may help you determine whether
your model truly outperforms the "clear sky" estimate by allowing you to target only cloudy days for
evaluation and comparison. You could also use it to compute general statistics on the input data, or even to
create a classification sub-task inside your model.

In the dataframe, this flag can only take five different values: "night", "cloudy", "slightly cloudy", "clear",
and "variable".

## Clearsky GHI estimations

The clearsky GHI estimates provided in the dataframe are based on the [the pvlib package](https://pvlib-python.readthedocs.io/en/stable/clearsky.html).
The model used is the one described by Ineichen and Perez (2002) in "A new airmass independent formulation for
the Linke turbidity coefficient" (doi:10.1016/S0038-092X(02)00045-2). Month-wise Linke turbidity factors are
queried for each station via latitude/longitude.

## Invalid data

As mentioned before, some entries of the dataframe may contain a "NaN" attribute instead of a GHI value or
an imagery file path. For increased safety, you should make sure to validate all imagery files regardless once
they are copied inside your team's directory (or once they are repackaged in your own intermediary format).

Remember also that the imagery itself might need to be padded if some pixels are missing for a specific timestamp.
