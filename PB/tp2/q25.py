def linha_montagem_3_linhas_dp(a, t, e, x, n):
    f = [[0] * n for _ in range(3)]
    l = [[0] * n for _ in range(3)]

    for i in range(3):
        f[i][0] = e[i] + a[i][0]

    for j in range(1, n):
        for i in range(3):
            tempos_anteriores = [f[k][j - 1] + t[k][j - 1] for k in range(3)]
            f[i][j] = a[i][j] + min(tempos_anteriores)
            l[i][j] = tempos_anteriores.index(min(tempos_anteriores))

    tempos_finais = [f[k][-1] + x[k] for k in range(3)]
    tempo_total_minimo = min(tempos_finais)
    melhor_caminho = tempos_finais.index(tempo_total_minimo)

    return tempo_total_minimo, melhor_caminho, l

a = [[7, 9, 3, 4], [8, 5, 6, 4], [3, 7, 2, 5]]
t = [[2, 3, 1, 3], [2, 1, 2, 2], [1, 2, 1, 2]]
e = [2, 4, 3]
x = [3, 2, 4]
n = len(a[0])

tempo_total_minimo, melhor_caminho, caminho_3_linhas = linha_montagem_3_linhas_dp(a, t, e, x, n)
print(f"Tempo total mínimo: {tempo_total_minimo}")
print(f"Caminho ótimo: {melhor_caminho}")
