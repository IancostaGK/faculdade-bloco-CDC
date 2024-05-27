from numba import jit, prange

@jit(nopython=True, parallel=True)
def generate_pascal_triangle(num_rows):
    pascal_triangle = [[1] * (row + 1) for row in range(num_rows)]
    
    for i in prange(1, num_rows):
        for j in prange(1, i):
            pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
    
    return pascal_triangle

num_rows = 10

triangle = generate_pascal_triangle(num_rows)

for row in triangle:
    print(row)
