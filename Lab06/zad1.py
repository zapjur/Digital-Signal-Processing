
# Import necessary libraries
import numpy as np
import scipy.io
import scipy.signal
import matplotlib.pyplot as plt

# Load the .mat file
data = scipy.io.loadmat('/Users/piotrzapior/Documents/GitHub/Digital-Signal-Processing/Lab06/butter.mat')

# Adjusting the extraction of z, p, k to ensure they are in the correct format
z = np.squeeze(data['z'])
p = np.squeeze(data['p'])
k = np.squeeze(data['k']).item()  # Assuming k is a scalar and making sure it's extracted as such

# Convert zero-pole-gain to transfer function form
b, a = scipy.signal.zpk2tf(z, p, k)

# Define constants
fs = 16000
fmin = 1189
fmax = 1229
wmin = 2 * np.pi * fmin
wmax = 2 * np.pi * fmax

# Digital filter design using bilinear transformation
num_d, den_d = scipy.signal.bilinear(b, a, fs)

# Generate frequency response for the digital filter
N = 1024  # Number of points in the frequency response
w, H = scipy.signal.freqz(num_d, den_d, N, fs=fs)

# Plot frequency response of the digital filter
plt.figure()
plt.plot(w, np.abs(H))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.title('Frequency Response of the Digital Filter')
plt.grid(True)
plt.axvline(x=fmin, color='r', linestyle='--')
plt.axvline(x=fmax, color='r', linestyle='--')

# Calculate and plot frequency response for the analog filter
w = np.logspace(np.log10(wmin), np.log10(wmax), 1000)
Hz = scipy.signal.freqs(b, a, w)

w, Hz = scipy.signal.freqs(b, a, w)  # This already splits the tuple into w and Hz correctly

plt.figure()
plt.semilogx(w, np.abs(Hz))
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Amplitude')
plt.title('Frequency Response of the Analog Filter')
plt.grid(True)
plt.axvline(x=wmin, color='r', linestyle='--')
plt.axvline(x=wmax, color='r', linestyle='--')

# Signal generation
duration = 1  # duration in seconds
t = np.arange(0, duration, 1/fs)
f1 = 1209
f2 = 1272
signal1 = np.sin(2 * np.pi * f1 * t)
signal2 = np.sin(2 * np.pi * f2 * t)
digital_signal = signal1 + signal2

# Custom filtering of the digital signal
filtered_signal = np.zeros_like(digital_signal)

for n in range(len(filtered_signal)):
    for k in range(len(num_d)):
        if n - k >= 0:
            filtered_signal[n] += num_d[k] * digital_signal[n - k]
    for k in range(1, len(den_d)):
        if n - k >= 0:
            filtered_signal[n] -= den_d[k] * filtered_signal[n - k]

# Plotting the original and filtered signals using the custom filter
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, digital_signal)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Digital Signal Consisting of Two Harmonics (Original)')

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Digital Signal After Filtering (Custom Filter)')

# Filtering the digital signal using the filter function
filtered_signal = scipy.signal.lfilter(num_d, den_d, digital_signal)

# Plotting the original and filtered signals using the filter function
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, digital_signal)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Digital Signal Consisting of Two Harmonics (Original)')

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Digital Signal After Filtering')

plt.show()
