import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import gdown

# URL pliku do pobrania
url = 'https://drive.google.com/uc?id=1DlFH_fB-T39E7ha00sGnWmcipyBAua3F'

# Ścieżka, pod którą chcesz zapisać pobrany plik
output_path = 'adsl_x.mat'

# Pobieranie pliku
gdown.download(url, output_path, quiet=False)

def mycorr(x, y):
    # Obliczanie korelacji wzajemnej dwóch wektorów
    # Korelację oblicza się jako sumę wartości obu sygnałów przemnożonych przez siebie
    # x, y - wektory wejściowe
    # r - wektor wynikowy korelacji wzajemnej
    # lags - opóźnienia dla każdej wartości w r
    n = len(x)
    m = len(y)

    # obliczenie średnich wartości obu wektorów
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # obliczenie odchyleń standardowych obu wektorów
    x_std = np.std(x)
    y_std = np.std(y)

    r = np.zeros(n + m - 1)
    lags = np.arange(-n + 1, m)

    # wyliczenie korelacji wzajemnej
    for i in range(len(r)):
        if lags[i] < 0:
            r[i] = np.sum((x[0:n + lags[i]] - x_mean) * (y[-lags[i]:m] - y_mean))
        elif lags[i] == 0:
            r[i] = np.sum((x - x_mean) * (y - y_mean))
        else:
            r[i] = np.sum((x[lags[i]:n] - x_mean) * (y[0:m - lags[i]] - y_mean))

        r[i] = r[i] / (x_std * y_std * (n - abs(lags[i])))

    return r

data = scipy.io.loadmat('adsl_x.mat')
x = np.array(data['x'])
prefix_len = 32  # długość prefiksu
frame_len = 512  # długość ramki
package_len = prefix_len + frame_len # długość ramki i prefiksu


max_corr = 0  # początkowa wartość maksymalnej korelacji
st_prefix_probe = np.zeros((3, 1))

for i in range(len(x) // 3):  # pętla po całym sygnale
    if (i + 3 * package_len) > len(x):
        break
        #

    max_corr_grup = 0
    tmp_prefix_probe = np.zeros((3, 1))

    for j in range(3):
      # według wykładu pakiety mają występować idealnie po sobie dlatego:
      # trzeba znaleść takie miejsca dla których suma 3 korelancji będzie największa
        prefix = x[i + j * package_len: i + j * package_len + prefix_len]  # prefiks
        tmp_prefix_probe[j, 0] = i + j * package_len

        copy_probe_block = x[i + j * package_len + frame_len: i + j * package_len + frame_len + prefix_len]
        # korelacja między pierwszymi 32 próbkami a ostatnimi 32 próbkami w oknie
        corr = mycorr(prefix, copy_probe_block)  # Moja funkcja korelacji

        max_corr_grup += np.mean(corr)

    if max_corr_grup > max_corr:  # jeśli korelacja jest większa niż dotychczasowa maksymalna
        max_corr = max_corr_grup  # aktualizacja maksymalnej korelacji
        st_prefix_probe = tmp_prefix_probe  # początek prefiksu

plt.plot(x)
for i in range(3):
    plt.plot(st_prefix_probe[i, 0], 0, 'rx')
plt.legend(['signal'])
plt.show()