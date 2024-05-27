def linha_montagem(a, t, e, x, n, linha_atual, estacao_atual):
    if estacao_atual == n:
        return x[linha_atual]  

    custo_estacao_atual = a[linha_atual][estacao_atual]
    custo_transferencia = t[linha_atual][estacao_atual]

    tempo_mesma_linha = custo_estacao_atual + linha_montagem(a, t, e, x, n, linha_atual, estacao_atual + 1)

    tempo_outra_linha = custo_estacao_atual + custo_transferencia + e[linha_atual] + linha_montagem(a, t, e, x, n, 1 - linha_atual, estacao_atual + 1)

    return min(tempo_mesma_linha, tempo_outra_linha)

a = [[7, 9, 3, 4], [8, 5, 6, 4]]
t = [[2, 3, 1, 3], [2, 1, 2, 2]]
e = [2, 4]
x = [3, 2]
n = len(a[0])

tempo_total = min(e[0] + linha_montagem(a, t, e, x, n, 0, 0), e[1] + linha_montagem(a, t, e, x, n, 1, 0))
print(f"Tempo total mínimo: {tempo_total}")
