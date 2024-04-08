
import numpy as np
from scipy.signal import butter, sosfilt, sosfreqz, spectrogram, periodogram, welch, sosfiltfilt
import matplotlib.pyplot as plt

# Define constants
fs = 3.2e6  # Sampling frequency
N = int(32e6)  # Number of IQ samples
fc = 0.50e6  # Center frequency of the FM station
bwSERV = 80e3  # Bandwidth of the FM service
bwAUDIO = 16e3  # Audio bandwidth

# Read IQ samples
f = open('/Users/piotrzapior/Documents/GitHub/Digital-Signal-Processing/Lab06/samples_100MHz_fs3200kHz.raw', 'rb')
s = np.random.randint(0, 255, 2*N, dtype='uint8') - 127

# Convert to complex IQ samples
wideband_signal = s[::2] + 1j * s[1::2]

# Precompute the frequency shift factor
# Assuming wideband_signal is N//2 samples long
freq_shift_factor = np.exp(-1j * 2 * np.pi * fc / fs * np.arange(len(wideband_signal)))

# Apply frequency shift
wideband_signal_shifted = wideband_signal * freq_shift_factor

# Filter design using SOS for numerical stability
sos = butter(4, bwSERV / (fs / 2), 'low', output='sos')

# Apply filtering
wideband_signal_filtered = sosfilt(sos, wideband_signal_shifted)

# Decimation
decimation_factor = int(fs / (2 * bwSERV))
wideband_signal_decimated = wideband_signal_filtered[::decimation_factor]

# FM Demodulation
dx = np.diff(wideband_signal_decimated)  # Use np.diff for efficiency
phase_diff = np.angle(dx)

# Anti-aliasing filter before final decimation
sos_aa = butter(4, bwAUDIO / (bwSERV / 2), 'low', output='sos')
y_filtered = sosfilt(sos_aa, phase_diff)

# Final decimation to match audio bandwidth
final_decimation_factor = int(bwSERV / bwAUDIO)
ym = y_filtered[::final_decimation_factor]

# Normalize audio signal
ym = ym - np.mean(ym)
ym = ym / (1.01 * np.max(np.abs(ym)))

# Plotting
plt.figure(figsize=(10, 8))

# Original Signal Spectrogram
plt.subplot(311)
f, t, Sxx = spectrogram(wideband_signal, fs, nperseg=1024)
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.title('Spectrogram of Original Signal')

# Filtered Signal Spectrogram
plt.subplot(312)
f, t, Sxx = spectrogram(wideband_signal_filtered, fs, nperseg=1024)
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.title('Spectrogram of Filtered Signal')

# Power Spectral Density using Welch's method
plt.subplot(313)
f, Pxx = welch(wideband_signal, fs, nperseg=1024)
plt.semilogy(f, Pxx)
plt.xlabel('Frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.title('PSD of Original Signal')

plt.tight_layout()
plt.show()