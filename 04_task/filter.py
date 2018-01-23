import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, freqz, butter, lfilter

class BandStopFilter(object):
    def __init__(self, fs, f0):
        self.Fs, self.F0 = fs, f0
        self.a = self.b = None

    def filter(self, signal):
        return signal.Fs, lfilter(self.b, self.a, signal.x)

    def display(self):
        # Frequency response
        w, h = freqz(self.b, self.a)
        # Generate frequency axis
        freq = w * self.Fs / (2 * np.pi)
        # Plot
        fig, ax = plt.subplots(2, 1, figsize=(8, 6))
        ax[0].plot(freq, 20 * np.log10(abs(h)), color='blue')
        ax[0].set_title("Frequency Response " + type(self).__name__)
        ax[0].set_ylabel("Amplitude (dB)", color='blue')
        ax[0].set_xlim([0, self.Fs // 2])
        ax[0].grid()

        ax[1].plot(freq, np.unwrap(np.angle(h)) * 180 / np.pi, color='green')
        ax[1].set_ylabel("Angle (degrees)", color='green')
        ax[1].set_xlabel("Frequency (Hz)")
        ax[1].set_xlim([0, self.Fs // 2])
        ax[1].set_yticks([-90, -60, -30, 0, 30, 60, 90])
        ax[1].set_ylim([-90, 90])
        ax[1].grid(), plt.show()


class NotchFilter(BandStopFilter):
    def __init__(self, fs, f0, qfactor=50):
        super().__init__(fs, f0)
        w0 = f0 / (fs / 2)
        self.b, self.a = iirnotch(w0, qfactor)

class ButterFilter(BandStopFilter):
    def __init__(self, fs, f0, order=5):
        super().__init__(fs, f0)
        nyq = 0.5 * fs
        low, high = (f0 - 1000) / nyq, (f0 + 1000) / nyq
        self.b, self.a = butter(order, [low, high], btype='stop')