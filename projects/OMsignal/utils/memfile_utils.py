import numpy as np


def read_memfile(filename, shape, dtype='float32'):
    # read binary data and return as a numpy array
    fp = np.memmap(filename, dtype=dtype, mode='r', shape=shape)
    data = np.zeros(shape=shape, dtype=dtype)
    data[:] = fp[:]
    del fp
    return data


def write_memfile(data, filename):
    # write a numpy array 'data' into a binary  data file specified by
    # 'filename'
    shape = data.shape
    dtype = data.dtype
    fp = np.memmap(filename, dtype=dtype, mode='w+', shape=shape)
    fp[:] = data[:]
    del fp
