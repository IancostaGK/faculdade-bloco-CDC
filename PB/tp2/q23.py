def linha_montagem_dp(a, t, e, x, n):
    f = [[0] * n for _ in range(2)]  
    l = [[0] * n for _ in range(2)]  

    f[0][0] = e[0] + a[0][0]
    f[1][0] = e[1] + a[1][0]

    for j in range(1, n):
        for i in range(2):
            if f[i][j - 1] + a[i][j] <= f[1 - i][j - 1] + t[1 - i][j - 1] + a[i][j]:
                f[i][j] = f[i][j - 1] + a[i][j]
                l[i][j] = i
            else:
                f[i][j] = f[1 - i][j - 1] + t[1 - i][j - 1] + a[i][j]
                l[i][j] = 1 - i

    tempo_total = min(f[0][-1] + x[0], f[1][-1] + x[1])
    melhor_caminho = [0] * n
    melhor_caminho[-1] = 0 if f[0][-1] + x[0] <= f[1][-1] + x[1] else 1

    for j in range(n - 2, -1, -1):
        melhor_caminho[j] = l[melhor_caminho[j + 1]][j + 1]

    return tempo_total, melhor_caminho

a = [[7, 9, 3, 4], [8, 5, 6, 4]]
t = [[2, 3, 1, 3], [2, 1, 2, 2]]
e = [2, 4]
x = [3, 2]
n = len(a[0])

tempo_total_minimo, melhor_caminho = linha_montagem_dp(a, t, e, x, n)
print(f"Tempo total mínimo: {tempo_total_minimo}")
print(f"Caminho ótimo: {melhor_caminho}")
