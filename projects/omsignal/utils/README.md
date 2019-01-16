# Utils

This folder contains utility functions that you may need throughout the project. It contains the following files:

## preprocessor.py

This file implements the `Preprocessor` class. It is a torch `nn.module` for normalizing an ECG signal. It can be used as the first layer in a model. **Back-prop** is not going through this module.
More specifically, the normalization is performed as follows: 
* First, the overall average of the signal is set to 0, and standard deviation set to 1.
* Then, the average is removed in a window of 2 seconds (250 points). This is because the average of the signal can shift over time.
* Finally, the signal is normalized (standard deviation = 1) over windows of 4 seconds, to remove shifts of the RMS signal. 

These recommendations come from OMSignal's experts. It is not recommended to tune these parameters (2 and 4 seconds), even if it is **not forbidden** to do so, especially if you obtain better performances.


## memfile_utils.py

This file contains utility functions for reading and writing `memory-map` from/to disk.


## fft_utils.py

This file contains utility functions for performing `fft` transformations on the ECG signal.

## spectrogram_utils.py

This file contains utility functions for performing `spectrogram` transformations on the ECG signal.


## scoring_function.py

This file contains the method for computing the metrics associated to the prediction values of your model with respect to ground truth data.

