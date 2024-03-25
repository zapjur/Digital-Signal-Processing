import numpy as np
import matplotlib.pyplot as plt

A = 230
f = 50
T = 1

fs1 = 10000
fs2 = 51 #26
fs3 = 50 #25
fs4 = 49 #24

t1 = np.arange(0, T, 1/fs1)
t2 = np.arange(0, T, 1/fs2)
t3 = np.arange(0, T, 1/fs3)
t4 = np.arange(0, T, 1/fs4)

y1 = A * np.sin(2 * np.pi * f * t1)
y2 = A * np.sin(2 * np.pi * f * t2)
y3 = A * np.sin(2 * np.pi * f * t3)
y4 = A * np.sin(2 * np.pi * f * t4)

plt.plot(t1, y1, 'b-', label='fs1 = ' + str(fs1) + 'Hz')
plt.plot(t2, y2, 'go', label='fs2 = ' + str(fs2) + 'Hz')
plt.plot(t3, y3, 'ro', label='fs3 = ' + str(fs3) + 'Hz')
plt.plot(t4, y4, 'ko', label='fs4 = ' + str(fs4) + 'Hz')
plt.xlabel('Czas [s]')
plt.ylabel('Napięcie [V]')
plt.title('Sinusoidy o różnych częstotliwościach próbkowania')
plt.legend()
plt.grid(True)
plt.show()