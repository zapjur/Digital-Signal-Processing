import numpy as np
import matplotlib.pyplot as plt

fs2 = 200
fs1 = 10000

dt2 = 1/fs2
dt1 = 1/fs1

time_fs2 = np.arange(0, 0.1, dt2)
time_fs1 = np.arange(0, 0.1, dt1)

y_fs2 = 230 * np.sin(2 * np.pi * 50 * time_fs2)
y_fs1 = 230 * np.sin(2 * np.pi * 50 * time_fs1)

y_out = np.zeros(len(time_fs1))

for i in range(len(time_fs1)):
    val = 0
    for n in range(len(time_fs2)):
        T1 = 1/fs2
        T2 = 1/fs1
        t = i * T2
        nT = n * T1
        y = np.pi/T1 * (t - nT)
        sinc = 1
        if y != 0:
            sinc = np.sin(y)/y
        val = val + y_fs2[n] * sinc
    y_out[i] = val

plt.figure()
plt.grid(True)
plt.plot(time_fs1, y_fs1, 'b-')
plt.plot(time_fs1, y_out, 'r-')
plt.xlabel('Czas (s)')
plt.ylabel('Amplituda (V)')
plt.title('Rekonstrukcja sygnału')
plt.legend(['Sygnał oryginalny', 'Sygnał zrekonstruowany'])

errors = np.abs(y_fs1 - y_out)
plt.figure()
plt.grid(True)
plt.plot(time_fs1, errors, 'k-')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [V]')
plt.title('Błędy rekonstrukcji sygnału sin(x)/x')
plt.legend(['Błędy rekonstrukcji'])

plt.show()