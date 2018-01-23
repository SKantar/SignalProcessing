import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

phases, labels = [0, np.pi / 4, np.pi / 2, np.pi], ['', '$\pi / 4$', '$\pi / 2$', '$\pi$']
Fs = N = 1200
T = 1.0 / Fs
x = np.linspace(T, N * T, N)

# I Component
f1, f2 = 130, 288
y1 = np.sin(f1 * 2.0 * np.pi * x)
y1f = fft(y1)

# II Component
for i, phase in enumerate(phases):
    y2 = np.sin(phase + f2 * 2.0 * np.pi * x)
    y2f = fft(y2)

    # Complete Component
    y = y1 + y2
    yf = fft(y)
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

    plt.figure(i + 1)
    # Module
    plt.subplot(3, 1, 1)
    plt.stem(xf, 2.0 / N * np.abs(yf[0:N//2]))
    plt.yticks([-1, -0.5, 0, 0.5, 1])
    plt.title('Module {}'.format(labels[i]), position=(0.9, 0.8))
    plt.grid()
    # Real
    plt.subplot(3, 1, 2)
    plt.stem(xf, 2.0 / N * np.real(yf[0:N // 2]))
    plt.yticks([-1, -0.5, 0, 0.5, 1])
    plt.title('Real {}'.format(labels[i]), position=(0.9, 0.8))
    plt.grid()
    # Imag
    plt.subplot(3, 1, 3)
    plt.stem(xf, 2.0 / N * np.imag(yf[0:N // 2]))
    plt.yticks([-1, -0.5, 0, 0.5, 1])
    plt.title('Imag {}'.format(labels[i]), position=(0.9, 0.8))
    plt.xlabel('Frequency [Hz]')
    plt.grid()
    plt.show(block=False)

