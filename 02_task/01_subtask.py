import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

Fs, N = 200, 150        # Sample frequence, Number of sample points
T = 1.0 / Fs            # Sample spacing
t = np.linspace(T, N * T, N)

A, f = 2.3, 3
x_clear = A * np.sin(f * 2.0 * np.pi * t)

powers, colors = [0, 1, 3, 6], ['r', 'g', 'b', 'y']
for i, power in enumerate(powers):
    e = np.random.normal(0, 1, N) * np.sqrt(power)
    x = x_clear + e
    xf = fft(x)

    yf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

    # Display FFT
    plt.figure(i + 1)
    plt.stem(yf, 2.0 / N * np.abs(xf[0:N // 2]), colors[i],
             markerfmt='{}o'.format(colors[i]))
    plt.title('FFT Spectrum AWGN Power {}'.format(powers[i]))
    plt.xlabel('Frequency [Hz]')
    plt.grid()
    plt.show()


