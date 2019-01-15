# OMsignal Data

Data for the projet is provided by OMsignal and therefore, it is **private**. The data is stored on the Helios server into the following directory:
* `/rap/jvb-000-aa/COURS2019/etudiants/data/omsignal/myHeartProject/`.


The provided data is split into 3 binary files:
* `MILA_TrainLabeledData.dat` - labeled data for supervised training
* `MILA_ValidationLabeledData.dat` -  labeled data for validation,
* `MILA_UnlabeledData.dat` -  unlabeled data.


Each labeled dataset (`MILA_TrainLabeledData.dat` and `MILA_ValidationLabeledData.dat`) contains 5 windows of 30 second length ECG data (sampled at 125 Hz) for each of the 32 participants. For each participant, the corresponding samples in the `MILA_TrainLabeledData.dat` and `MILA_ValidationLabeledData.dat` datasets have **not** been collected the **same** day. Similarly, the dataset on which your script will be evaluated contains, for each participant, samples collected on a **different** day too.


For the labeled datasets (`MILA_TrainLabeledData.dat` and `MILA_ValidationLabeledData.dat`), the description of the provided data is as follows:
* `Shape = 160 x 3754` - where `160 = 5 x 32 ` corresponds to the number of windows.
* `Column 0` to `Column 3749` - Columns corresponding to the ECG data ( `30 seconds x 125 Hz = 3750` ). They contain `float` values.
* `Column 3750` - Columns corresponding to the `PR_Mean` of the corresponding ECG sample. It contains `float` values.
* `Column 3751` - Columns corresponding to the `RT_Mean` of the corresponding ECG sample. It contains `float` values.
* `Column 3752` - Columns corresponding to the `RR_StdDev` of the corresponding ECG sample. It contains `float` values.
* `Column 3753` - Columns corresponding to the `ID` of the participant. It contains `int` values.

The description of the unlabeled dataset (`MILA_UnlabeledData.dat`) is as follows:
* `Shape = 657233 x 3750` - where `657233 ` corresponds to the remaining number of unlabeled windows.
* `Column 0` to `Column 3749` - Columns corresponding to the ECG data ( `30 seconds x 125 Hz = 3750` ). They contain `float` values.


For Block 1, only labeled datasets (`MILA_TrainLabeledData.dat` and `MILA_ValidationLabeledData.dat`) should be considered. The unlabeled dataset is used for the unsupervised parts of Blocks `2` and `3`. 


## User ID

In the labeled datasets, the `max` value of the `ID` is `43` and the `min` value is `0`. However, there is only `32` participants. For the classification task, you ** must ** define a map of the provided IDs to classes that belong to the range `0 -- 31`.
** ATTENTION: ** when reporting your results for final evaluation, you ** must remapping back ** your predicted classes to the original values, otherwise you may have **bad surprises**.

# Dataset Loading

Datasets are provided as a `memory-map` (`numpy.memmap`). To read them, use the following:

## Generic Script

```
def read_memfile(filename, shape, dtype='float32'):
    # read binary data and return as a numpy array
    fp = np.memmap(filename, dtype=dtype, mode='r', shape=shape)
    data = np.zeros(shape=shape, dtype=dtype)
    data[:] = fp[:]
    del fp
    return data

```

## Labeled Datasets

```
trainDataset = read_memfile('MILA_TrainLabeledData.dat', shape=(160, 3754), dtype='float32')
validDataset = read_memfile('MILA_ValidationLabeledData.dat', shape=(160, 3754), dtype='float32')
```

## Unlabeled Dataset

```
unlabeledDataset = read_memfile('MILA_UnlabeledData.dat', shape=(657233, 3750), dtype='float32')
```


This script is provided in the following GitHub path of the project: `utils/memfile_utils.py`. 


# Evaluation

Your script will be evaluated on a blind test set `MILA_UnlabeledTestData.dat` of shape `160 x 3750` and you are required to produce your result as a `memory-map` of shape `160 x 4` in the same order as the test file and whose columns correspond to:

you are required in this project to provide your result as 
* `Column 0` - predicted `PR_Mean` of the corresponding ECG sample. 
* `Column 1` - predicted `RT_Mean` of the corresponding ECG sample. 
* `Column 2` - predicted `RR_StdDev` of the corresponding ECG sample. 
* `Column 3` - predicted `ID` of the participant to which the ECG sample belongs.

To save a `memory-map`, use the following:
```
def write_memfile(data, filename):
    # write a numpy array 'data' into a binary  data file specified by
    # 'filename'
    shape = data.shape
    dtype = data.dtype
    fp = np.memmap(filename, dtype=dtype, mode='w+', shape=shape)
    fp[:] = data[:]
    del fp

```

This script is provided in the following GitHub path of the project: `utils/memfile_utils.py`. 


