import numpy as np
import matplotlib.pyplot as plt

# Define poles and zeros
p12 = -0.5 + 9.5j
p34 = -1 + 10j
p56 = -0.5 + 10.5j
z12 = 5j
z34 = 15j

# Duplicate poles and zeros with their conjugates
p = [p12, p34, p56, np.conj(p12), np.conj(p34), np.conj(p56)]
z = [z12, z34, np.conj(z12), np.conj(z34)]

# Amplification factor
wzm = 0.42

# Plot poles and zeros
plt.figure(figsize=(8, 6))
plt.plot(np.real(p), np.imag(p), "o", label="Poles")
plt.plot(np.real(z), np.imag(z), "x", label="Zeros")
plt.grid(True)
plt.axis('equal')
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.title("Poles and Zeros")
plt.legend()

# Get polynomial coefficients from roots
a = np.poly(p)
b = np.poly(z) * wzm

# Linear frequency response
w = np.arange(4, 16.1, 0.1)
s = w * 1j
Hlinear = np.abs(np.polyval(b, s) / np.polyval(a, s))

# Plot linear frequency response
plt.figure()
plt.plot(w, Hlinear)
plt.xlabel("Frequency [rad/s]")
plt.ylabel("|H(jw)|")
plt.title("Linear Frequency Response")

# Logarithmic frequency response
Hlog = 20 * np.log10(Hlinear)
plt.figure()
plt.semilogx(w, Hlog, 'r')
plt.xlabel("Frequency [rad/s]")
plt.ylabel("20log10(|H(jw)|)")
plt.title("Logarithmic Frequency Response")

# Phase response
H_phase = np.angle(np.polyval(b, s) / np.polyval(a, s))
plt.figure()
plt.plot(w, H_phase, 'g')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Angle [rad]')
plt.title('Phase-Frequency Characteristic')
plt.grid(True)

plt.show()
