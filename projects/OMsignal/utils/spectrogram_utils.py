import numpy as np
from scipy import signal


def make_spectogram(x, lognorm=False, fs=16, nperseg=256, noverlap=None):
    # takes a time-series x and returns the spectogram
    # input:
    #        x: time series
    #        lognorm: bool - log spectrogram or not (default: False)
    #        fs: float - Sampling frequency of the x time series.
    #             Defaults to 16.
    #        nperseg: int - Length of each segment (default: 256).
    #        noverlap: int, Number of points to overlap between segments.
    #               If None, noverlap = nperseg // 8. Defaults to None.
    # output :
    #       f : ndarray - Array of sample frequencies.
    #       t : ndarray  - Array of segment times.
    #       Zxx : ndarray - Spectrogram of x.
    #           By default, the last axis of Zxx corresponds
    #           to the segment times.

    f, t, Zxx = signal.spectrogram(
        x, fs=fs, nperseg=nperseg, noverlap=noverlap
    )
    if lognorm:
        Zxx = np.abs(Zxx)
        mask = Zxx > 0
        Zxx[mask] = np.log(Zxx[mask])
        Zxx = (Zxx - np.min(Zxx)) / (np.max(Zxx) - np.min(Zxx))

    return f, t, Zxx


def plot_spectrogram(f, t, Zxx):
    import matplotlib.pyplot as plt
    plt.switch_backend('agg')

    plt.title('Spectrogram')
    plt.pcolormesh(t, f, Zxx, vmin=0, vmax=1)
    plt.ylabel('Frequency')
    plt.xlabel('Time')
    plt.savefig('stft.png')
    plt.close()


if __name__ == '__main__':

    # only for testing; this reads and create a plot of an Spectogram
    fake_ecg = np.random.randn(3750).astype(np.float32)
    f, t, Zxx = make_spectogram(fake_ecg, True)
    plot_spectrogram(f, t, Zxx)
