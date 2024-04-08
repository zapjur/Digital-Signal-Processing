import numpy as np
import scipy.io
import scipy.signal
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the filter coefficients from 'butter.mat'
data = scipy.io.loadmat('/Users/piotrzapior/Documents/GitHub/Digital-Signal-Processing/Lab06/butter.mat')
z, p, k = [np.squeeze(data[param]) for param in ('z', 'p', 'k')]

# Convert zero-pole-gain to transfer function form
b, a = scipy.signal.zpk2tf(z, p, k)

# Define constants and design the digital filter using bilinear transformation
fs = 16000
num_d, den_d = scipy.signal.bilinear(b, a, fs)

# Load an audio file (replace 'path/to/your/audio_file.wav' with the actual file path)
fs, s = wavfile.read('/Users/piotrzapior/Documents/GitHub/Digital-Signal-Processing/Lab06/sounds/s2.wav')

# Apply the digital filter to the audio signal
filtered_signal = scipy.signal.lfilter(num_d, den_d, s)

# Plot spectrograms before and after filtering
plt.figure(figsize=(10, 8))

# Before filtering
plt.subplot(2, 1, 1)
plt.specgram(s, NFFT=4096, Fs=fs, noverlap=4096-512)
plt.title('Spectrogram Before Filtering')
plt.ylabel('Frequency [Hz]')

# After filtering
plt.subplot(2, 1, 2)
plt.specgram(filtered_signal, NFFT=4096, Fs=fs, noverlap=4096-512)
plt.title('Spectrogram After Filtering')
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')

plt.tight_layout()

# Plotting signals in the time domain
t = np.arange(len(s)) / fs
plt.figure(figsize=(10, 6))
plt.plot(t, s, label='Before Filtering')
plt.plot(t, filtered_signal, label='After Filtering', color='red')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend(['Before Filtering', 'After Filtering'])
plt.title('Signals in Time Domain')
plt.show()
