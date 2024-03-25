import numpy as np
import matplotlib.pyplot as plt

A = 230
f = 50
T = 0.1

fs1 = 10000
fs2 = 500
fs3 = 200

t1 = np.arange(0, T, 1/fs1)
t2 = np.arange(0, T, 1/fs2)
t3 = np.arange(0, T, 1/fs3)

y1 = A * np.sin(2 * np.pi * f * t1)
y2 = A * np.sin(2 * np.pi * f * t2)
y3 = A * np.sin(2 * np.pi * f * t3)

plt.plot(t1, y1, 'b-', label='fs1 = ' + str(fs1) + 'Hz')
plt.plot(t2, y2, 'ro', label='fs2 = ' + str(fs2) + 'Hz')
plt.plot(t3, y3, 'kx', label='fs3 = ' + str(fs3) + 'Hz')
plt.xlabel('Czas [s]')
plt.ylabel('Napięcie [V]')
plt.title('Sinusoidy o różnych częstotliwościach próbkowania')
plt.legend()
plt.grid(True)
plt.show()