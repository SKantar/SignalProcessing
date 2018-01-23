import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import kaiserord, firwin, freqz, lfilter, tf2zpk, group_delay
from scipy.fftpack import fft
from zplane import zplane

Fs = 1200
N = 512

T = 1.0 / Fs
t = np.linspace(T, N * T, N)

x = 2 * np.sin(2 * np.pi * 200 * t) + 2.5 * np.sin(2 * np.pi * 400 * t)

Fpass = 200.0
Fstop = 400.0
Apass = 1.0
Astop = 70.0
flag = 'scale'


nyq_rate = Fs / 2.0
M, beta = kaiserord(Astop, (Fstop - Fpass) / nyq_rate)
M, beta = 28, 7.1

cutoff_hz = (Fpass + Fstop) / 2
taps = firwin(M, cutoff_hz/nyq_rate, window=('kaiser', beta))
w, h = freqz(taps)

# Amplitude and Phase response
fig = plt.figure()
plt.title('Digital filter frequency response')

# Aplitude
ax1 = fig.add_subplot(111)
plt.plot((w/np.pi/2) * Fs, -20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitude attenuation[dB]', color='b')
plt.xlabel('Frequency [rad/sample]')

# Phase
ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
plt.plot((w/np.pi/2) * Fs, angles, 'g')
plt.ylabel('Angle (radians)', color='g')
plt.grid()
plt.axis('tight')
plt.show()

# Poles and zeros
z, p, k = tf2zpk(taps, 1.0)

plt.figure()
zplane(z, p)
plt.grid(True, color='0.9', linestyle='-', which='both', axis='both')
plt.title('Poles and zeros')

# Group delay
w1, gd = group_delay((taps, 1.0))
plt.figure()
plt.title('Digital filter group delay')
plt.plot((w/np.pi/2) * Fs, gd)
plt.ylabel('Group delay [samples]')
plt.xlabel('Frequency [Hz]')
plt.grid(True, color='0.9', linestyle='-', which='both', axis='both')
plt.show()

# Filter Signal
filtered_x = lfilter(taps, 1.0, x)

# Display original and filtered signal
plt.figure()
plt.plot(t, x, 'g', label='UnFiltered')
plt.plot(t, filtered_x, 'r', label='Filtered')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.grid()
plt.show()

# Calculate FFT
X = fft(x)
filtered_X = fft(filtered_x)

y = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

# Display FFT
plt.figure()
unfiltered = plt.stem(y, 2.0 / N * np.abs(X[0:N//2]), 'g', markerfmt='go', label='UnFiltered')
filtered = plt.stem(y, 2.0 / N * np.abs(filtered_X[0:N//2]), 'r', markerfmt='ro', label='Filtered')
plt.legend(handles=[filtered, unfiltered], prop={'size': 16})
plt.title('FFT Spectrum')
plt.xlabel('Frequency [Hz]')
plt.grid()
plt.show()






