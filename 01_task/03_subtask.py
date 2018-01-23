import numpy as np
import matplotlib.pyplot as plt

from scipy.fftpack import fft

Fs = 1200       # Sample frequence
N = 50          # Number of sample points
T = 1.0 / Fs    # Sample spacing
x = np.linspace(T, N * T, N)

# I Component
f1 = 130
y1 = np.sin(f1 * 2.0 * np.pi * x)

# II Component
f2 = 288
y2 = np.sin(f2 * 2.0 * np.pi * x)

# Complete Component
y = y1 + y2
Y = fft(y)

xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

# Display FFT
plt.figure(1)
plt.stem(xf, 2.0 / N * np.abs(Y[0:N//2]))
plt.title('FFT Spectrum\n$x(t) = \sin(2\pi130t) + \sin(2\pi288t)$')
plt.xlabel('Frequency [Hz]')
plt.grid()
plt.show()