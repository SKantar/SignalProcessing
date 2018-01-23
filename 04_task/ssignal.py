import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile

class Signal(object):
    def __init__(self, x):
        self.Fs, self.x = x
        self.T, self.N = 1.0 / self.Fs, len(self.x)

    @staticmethod
    def read(filename):
        return wavfile.read(filename)

    def store(self, filename):
        wavfile.write(filename, self.Fs, self.x)

    def _display(self, y, x, title, xlabel, ylabel):
        plt.figure()
        plt.title(title)
        plt.plot(y, x)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.show()

    def display(self, title=''):
        t = np.linspace(self.T, self.N * self.T, self.N)
        self._display(
            y=t,
            x=self.x,
            title=title,
            xlabel='Time(s)',
            ylabel='Amplitude'
        )

    def display_fft(self, title=''):
        fftX = fft(self.x)
        yf = np.linspace(0.0, 1.0 / (2.0 * self.T), self.N // 2)
        self._display(
            y=yf,
            x=2.0 / self.N * np.abs(fftX[0:self.N // 2]),
            title=title + " FFT",
            xlabel='Frequency [Hz]',
            ylabel=''
        )
