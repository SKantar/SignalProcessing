import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def GCD(A, B):
    """ Greatest common divisor """
    while B:
        A, B = B, A % B
    return A


def LCM(A, B):
    """ Lowest common denominator """
    return A * B / GCD(A, B)


Fs = 1200   # Sample frequency
f1 = 130    # Frequency of 1st component
f2 = 288    # Frequency of 2nd component

# Number of sample points
N = int(LCM(Fs / GCD(Fs, f1), Fs / GCD(Fs, f2)))    # 600

T = 1.0 / Fs    # Sample spacing
x = np.linspace(T, N * T, N)

# I Component
y1 = np.sin(f1 * 2.0 * np.pi * x)

# II Component
y2 = np.sin(f2 * 2.0 * np.pi * x)

# Complete Signal
y = y1 + y2
yf = fft(y)

xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

# Display FFT
plt.figure()
plt.stem(xf, 2.0 / N * np.abs(yf[0:N//2]))
plt.title('FFT Spectrum\n$x(t) = \sin(2\pi130t) + \sin(2\pi288t)$')
plt.xlabel('Frequency [Hz]')
plt.grid()
plt.show()

