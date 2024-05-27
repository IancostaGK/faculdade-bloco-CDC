from numba import njit
import numpy as np

@njit(parallel=True)
def produto_escalar(vetor1, vetor2):
    resultado = 0
    for i in range(len(vetor1)):
        resultado += vetor1[i] * vetor2[i]
    return resultado

vetor1 = np.random.rand(1000)
vetor2 = np.random.rand(1000)

resultado = produto_escalar(vetor1, vetor2)
print("Produto escalar:", resultado)
