from cython.parallel import parallel, prange
import numpy as np
import time

def matrix_multiply_openmp(matrix1, matrix2):
    if matrix1.shape[1] != matrix2.shape[0]:
        raise ValueError("Número de colunas da primeira matriz não corresponde ao número de linhas da segunda matriz.")

    result = np.zeros((matrix1.shape[0], matrix2.shape[1]))

    with parallel():
        for i in prange(matrix1.shape[0]):
            for j in range(matrix2.shape[1]):
                for k in range(matrix1.shape[1]):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

if __name__ == "__main__":
    matrix1 = np.random.randint(1, 10, size=(100, 100))
    matrix2 = np.random.randint(1, 10, size=(100, 100))

    start_time = time.time()
    result = matrix_multiply_openmp(matrix1, matrix2)
    end_time = time.time()

    print(f"Tempo de execução: {end_time - start_time} segundos.")
