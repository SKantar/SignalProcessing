import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

Fs = 1200   # Sample frequence
N = 300     # Number of sample points
T = 1.0 / Fs
t = np.linspace(T, N * T, N)

# I Component
f1 = 130
x1 = np.sin(f1 * 2.0 * np.pi * t)

# II Component
f2 = 288
x2 = np.sin(f2 * 2.0 * np.pi * t)

# Complete Component
x = x1 + x2

# Display
plt.figure(1)
plt.plot(t, x2)
plt.grid()
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
title = "\sin(2 \omega {} t) + \sin(2 \omega {} t)".format(f1, f2)
plt.title("$x(t) = {}$".format(title))
plt.show()
