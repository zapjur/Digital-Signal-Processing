import numpy as np
import matplotlib.pyplot as plt

fs = 100
T = 1
A = 1

t = np.arange(0, T, 1/fs)

for f in range(0, 301, 5):
    y = A * np.sin(2 * np.pi * f * t)
    plt.figure(figsize=(10, 2))
    plt.plot(t, y)
    plt.title(f'Sinusoida o częstotliwości {f} Hz (Obieg {f//5 + 1})')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.grid(True)
    plt.show()

frequencies_to_compare = [[5, 105, 205], [95, 195, 295], [95, 105]]

def compare_frequencies(frequencies, signal_type='sin'):
    t = np.arange(0, T, 1/fs)
    plt.figure(figsize=(10, 6))
    for f in frequencies:
        if signal_type == 'sin':
            y = A * np.sin(2 * np.pi * f * t)
        else:
            y = A * np.cos(2 * np.pi * f * t)
        plt.plot(t, y, label=f'{f} Hz')
    plt.title(f'Porównanie {signal_type}usoid dla częstotliwości: {", ".join(map(str, frequencies))}')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.legend()
    plt.grid(True)
    plt.show()

frequencies_to_compare = [[5, 105, 205], [95, 195, 295], [95, 105]]

for frequencies in frequencies_to_compare:
    compare_frequencies(frequencies, 'sin')

for frequencies in frequencies_to_compare:
    compare_frequencies(frequencies, 'cos')
