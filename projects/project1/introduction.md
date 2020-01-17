# GHI Nowcasting Introduction

Note: this is a recap of some of the presentation slides available [here](@@@TODO@@@).

## Goal

Use satellite imagery ([GOES-13](https://en.wikipedia.org/wiki/GOES_13)) and any other relevant
metadata to predict [Global Horizontal Irradiance (GHI)](https://en.wikipedia.org/wiki/Solar_irradiance)
values as measured by seven [SURFRAD](https://www.esrl.noaa.gov/gmd/grad/surfrad/) stations in
the continental US.

The GHI at a specific geolocation depends on multiple factors including elevation, cloud cover,
surrounding land cover, turbidity, and air particles. The efficiency of solar panels can be tied
to the GHI. It can also be used in climate modeling.

Multiple GHI prediction models exist, but not all of them rely on satellite imagery. So-called
"clear sky" models rely on physical and mathematical models and can be used to estimate the
approximate GHI upper bound for any position on earth. These can serve as an auxiliary input
data source for imagery-based models.

The prediction horizon of interest for the project is ``[T_0, T_0 + 1h, T_0 + 3h, T_0 + 6h]``.
In other words, given a timestamp ``T_0``, we ask you to provide GHI values for that timestamp
as well as 1, 3, and 6 hours in the future. Due to the short-term nature of these predictions,
this is a called a "[nowcasting](<https://en.wikipedia.org/wiki/Nowcasting_(meteorology)>)" task.
To respect the nature of this problem, predictions for a given ``T_0`` timestep should **never**
rely on "future" imagery, that is imagery captured after ``T_0``. Models can however rely
on ``T_0`` as well as any timestep before that.

The idea behind using satellite imagery for GHI nowcasting is that some atmospheric phenomena
(e.g. clouds, particles) might be easier to track that way.

For this project, we are only evaluating our models at specific points on the map (i.e. at SURFRAD
stations). Ultimately, however, we are interested in models that can generalize to predict GHIs at
any point on the map. As such, you can only use data that would be available for the entirety of
the map. This means that your model cannot rely on past GHI values measured by stations on the
ground, since these would not be available at every point of the map.

## GOES-13, SURFRAD, and other metadata

We will provide all teams with preprocessed [GOES-13](https://en.wikipedia.org/wiki/GOES_13)
imagery. This imagery possesses five usable channels spanning the electromagnetic spectrum from
visible light to Mid-Infrared (MIR). GOES-13 imagery is geostationary and projected to a fixed
coordinate space. This means that image registration is not necessary between different
acquisition timestamps. This data is described in more detail [here](datasources.md).

A visualization of the GOES-13 imagery along with the measured GHI of the SURFRAD stations is
available [here](https://drive.google.com/file/d/12myylJZ_pDEORjvMpoHv-10O4HZIwW2y).

GOES-13 imagery is available from April 2010 to December 2016, inclusively, at 15-minute intervals.
The availability of this data is not perfect, and some files may be missing. The imagery channels
themselves may also contain pixels tagged as "missing" or "unavailable". It will be up to you to
handle these edge cases (filling in missing values, dealing with NaNs, etc.). You will have access
to the data ranging from April 2010 to December 2015, inclusively. The 2016 data is reserved for our
final (blind) test set. While this is technically publicly available data, we ask you
**not to use 2016 data to train your models**.

The SURFRAD stations provide GHI measurements at 1-minute intervals. To simplify the registration
of GOES-13 and SURFRAD data sources and to ensure uniformity among data, we provide a
[metadata catalog](dataframe.md) in the form of a Pandas dataframe. In that dataframe, the SURFRAD
measurements are smoothed to 15-minute intervals using a moving average. The SURFRAD measurements
may also contain missing values in the form of NaNs. Once again, it is up to the students to handle
these issues.

Finally, the provided metadata catalog includes daytime flags, clear sky GHI estimates and
cloudiness flags for all 15-minute entries. More information on these is provided [here](dataframe.md).

## Evaluation

Refer to the [evaluation page](evaluation.md).
