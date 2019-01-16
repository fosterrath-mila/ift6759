import numpy as np


def make_fft(x):
    # takes a time-series x and returns the FFT
    # input: x
    # output : R and I; real and imaginary componenet of the real FFT
    y = np.fft.rfft(x)
    return np.real(y), np.imag(y)


def plot_ecgfft(x, y):
    import matplotlib.pyplot as plt
    plt.switch_backend('agg')

    # plots the real and imaginary part of the FFT of an ECG signal
    plt.title('ECG FFT')
    plt.plot(x[0, 0, :])
    plt.plot(y[0, 0, :])
    plt.xlabel('Frequency')
    plt.ylabel('FFT')
    plt.legend(['Real', 'Imag'])
    plt.savefig('fft_visual.png')
    plt.close()

if __name__ == '__main__':
    # only for testing; this reads and create a plot of an FFT
    fake_ecg = np.random.randn(3750).astype(np.float32)
    fftr, ffti = make_fft(fake_ecg)
    plot_ecgfft(fftr, ffti)
