def linha_montagem_3_linhas(a, t, e, x, n, linha_atual, estacao_atual):
    if estacao_atual == n: 
        return x[linha_atual] 

    custo_estacao_atual = a[linha_atual][estacao_atual]
    custo_transferencia = t[linha_atual][estacao_atual]

    tempo_mesma_linha = custo_estacao_atual + linha_montagem_3_linhas(a, t, e, x, n, linha_atual, estacao_atual + 1)

    tempos_outras_linhas = []
    for outra_linha in range(3):
        if outra_linha != linha_atual:
            tempo_outra_linha = custo_estacao_atual + custo_transferencia + e[linha_atual] + \
                                linha_montagem_3_linhas(a, t, e, x, n, outra_linha, estacao_atual + 1)
            tempos_outras_linhas.append(tempo_outra_linha)

    return min(tempo_mesma_linha, *tempos_outras_linhas)

a = [[7, 9, 3, 4], [8, 5, 6, 4], [3, 7, 2, 5]]
t = [[2, 3, 1, 3], [2, 1, 2, 2], [1, 2, 1, 2]]
e = [2, 4, 3]
x = [3, 2, 4]
n = len(a[0])

tempo_total = min(e[0] + linha_montagem_3_linhas(a, t, e, x, n, 0, 0),
    e[1] + linha_montagem_3_linhas(a, t, e, x, n, 1, 0),
    e[2] + linha_montagem_3_linhas(a, t, e, x, n, 2, 0))
print(f"Tempo total mínimo: {tempo_total}")
