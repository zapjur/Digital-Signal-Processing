import numpy as np

N = 20

def generate_dct_ii_matrix(N):
    matrix = np.zeros((N, N))
    for k in range(N):
        for n in range(N):
            if k == 0:
                matrix[k, n] = np.sqrt(1/N)
            else:
                matrix[k, n] = np.sqrt(2/N) * np.cos((np.pi * k * (2*n + 1)) / (2 * N))
    return matrix

dct_ii_matrix = generate_dct_ii_matrix(N)

# Iloczyn skalarny każdej pary różnych wektorów powinien wynosić 0, a każdego wektora z samym sobą 1
is_orthonormal = True

for i in range(N):
    for j in range(i, N):
        dot_product = np.dot(dct_ii_matrix[i], dct_ii_matrix[j])

        if i == j:
            # Dla tej samej pary wektorów oczekujemy wartości 1
            if not np.isclose(dot_product, 1):
                is_orthonormal = False
                break
        else:
            # Dla różnych wektorów oczekujemy wartości bliskiej 0
            if not np.isclose(dot_product, 0):
                is_orthonormal = False
                break

    if not is_orthonormal:
        break


print(f"Czy macierz DCT-II jest ortonormalna? {is_orthonormal}")

