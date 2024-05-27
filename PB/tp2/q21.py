from cython.parallel import prange

def fibonacci_parallel(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        a, b = 0, 1
        for _ in prange(2, n, nogil=True):
            a, b = b, a + b
            fib_sequence.append(b)
        return fib_sequence

fib_seq_sequential = fibonacci_parallel(30)

print("Sequência de Fibonacci (sequencial):", fib_seq_sequential)