import numpy as np
from scipy.signal import butter, cheby1, cheby2, ellip, freqs, zpk2tf
import matplotlib.pyplot as plt

# Initial setup
sampling_freq = 256e3  # Sampling frequency of the A/D converter
cutoff = sampling_freq / 2
points = 4096
w = np.linspace(0, sampling_freq, points) * 2 * np.pi

# Filter requirements
freq_64 = 64e3
freq_112 = 112e3
freq_128 = 128e3

# Butterworth Filter Design
z_butter, p_butter, k_butter = butter(N=7, Wn=2 * np.pi * freq_64, analog=True, output='zpk')
b_butter, a_butter = zpk2tf(z_butter, p_butter, k_butter)
frequency_response_butter = freqs(b_butter, a_butter, w)

# Chebyshev Type I Filter Design
z_cheby1, p_cheby1, k_cheby1 = cheby1(N=5, rp=3, Wn=2 * np.pi * freq_64, analog=True, output='zpk')
b_cheby1, a_cheby1 = zpk2tf(z_cheby1, p_cheby1, k_cheby1)
frequency_response_cheby1 = freqs(b_cheby1, a_cheby1, w)

# Chebyshev Type II Filter Design
z_cheby2, p_cheby2, k_cheby2 = cheby2(N=5, rs=40, Wn=2 * np.pi * freq_112, analog=True, output='zpk')
b_cheby2, a_cheby2 = zpk2tf(z_cheby2, p_cheby2, k_cheby2)
frequency_response_cheby2 = freqs(b_cheby2, a_cheby2, w)

# Elliptic Filter Design
z_ellip, p_ellip, k_ellip = ellip(N=3, rp=3, rs=40, Wn=2 * np.pi * freq_64, analog=True, output='zpk')
b_ellip, a_ellip = zpk2tf(z_ellip, p_ellip, k_ellip)
frequency_response_ellip = freqs(b_ellip, a_ellip, w)

# Plotting Frequency Responses
plt.figure()
for response, label in zip(
        [frequency_response_butter, frequency_response_cheby1, frequency_response_cheby2, frequency_response_ellip], 
        ["Butter", "Czeby1", "Czeby2", "Elipt"]):
    plt.plot(w / (2 * np.pi * 1e3), 20 * np.log10(np.abs(response[1]) + 1e-12), label=label) 
plt.axis([0, 256, -40, 5])
plt.grid(True)
plt.title("Odpowiedź częstotliwościowa modelów")
plt.xlabel("Częstotliwość (kHz)")
plt.ylabel("Odpowiedź (dB)")
plt.legend()

# Plotting Pole Positions
plt.figure(figsize=(6, 6))
for poles, label in zip([p_butter, p_cheby1, p_cheby2, p_ellip], ["Butter", "Czeby1", "Czeby2", "Elipt"]):
    plt.plot(np.real(poles), np.imag(poles), 'o', label=label)
plt.title("Rozkład biegunów filtrów")
plt.xlabel("Re")
plt.ylabel("Im")
plt.legend()
plt.grid(True)
plt.axis('equal')

plt.show()
