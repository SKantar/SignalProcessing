import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

new_sizes = [200, 300, 400, 500]

Fs = 200
SN = 200    # Starting Number of sample points
T = 1.0 / Fs
t = np.linspace(T, SN * T, SN)

A = 2.3
f = 3
sx = A * np.sin(f * 2.0 * np.pi * t)

power = 3

for i, N in enumerate(new_sizes):
    x = np.pad(sx, (0, N - SN), 'constant')
    e = np.random.normal(0, 1, N) * np.sqrt(power)

    x = x + e
    xf = fft(x)

    yf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

    # Display FFT
    plt.figure(i + 1)
    plt.stem(yf, 2.0 / N * np.abs(xf[0:N // 2]))
    plt.title('FFT Spectrum AWGN Power 3, Number of sample points'.format(N))
    plt.xlabel('Frequency [Hz]')
    plt.grid()
    plt.show()


