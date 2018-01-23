import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

new_sizes = [800, 1000, 1200]

Fs, SN = 1200, 600
T = 1.0 / Fs

sx = np.linspace(T, SN * T, SN)

for i, N in enumerate(new_sizes):
    x = np.pad(sx, (0, N - SN), 'constant')

    # I Component
    f1 = 130
    y1 = np.sin(f1 * 2.0 * np.pi * x)
    y1f = fft(y1)

    # II Component
    f2 = 288
    y2 = np.sin(f2 * 2.0 * np.pi * x)
    y2f = fft(y2)

    # Complete Component
    y = y1 + y2
    yf = fft(y)

    xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

    plt.figure(i + 1)
    plt.stem(xf, 2.0 / N * np.abs(yf[0:N//2]))
    plt.title('FFT Spectrum N = {}'.format(N))
    plt.xlabel('Frequency [Hz]')
    plt.grid()
    plt.show()



