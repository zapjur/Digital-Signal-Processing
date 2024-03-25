import numpy as np

def generate_dct_ii_matrix(N):
    matrix = np.zeros((N, N))
    for k in range(N):
        for n in range(N):
            if k == 0:
                matrix[k, n] = np.sqrt(1/N)
            else:
                matrix[k, n] = np.sqrt(2/N) * np.cos((np.pi * k * (2*n + 1)) / (2 * N))
    return matrix

N = 20
A = generate_dct_ii_matrix(N)
S = np.transpose(A)

I = np.dot(S, A)
tolA = np.max(np.abs(S - np.linalg.inv(A)))

isidentic = True

for o in range(N):
    for p in range(N):
        if abs(I[o, p]) != 0 and o != p:
            isidentic = False

        if abs(I[o, p]) != 1 and o == p:
            isidentic = False

if isidentic:
    print(f'Macierz I jest identycznościowa z błędem: {tolA}')
else:
    print('Macierz I nie jest identycznościowa')

srand = np.random.rand(N)
X = np.dot(A, srand)

rcnst = np.dot(S, X)

tolB = np.max(np.abs(srand - rcnst))

if tolB < 1e-10:
    print(f'Rekonstrukcja sygnału z błędem: {tolB}')
