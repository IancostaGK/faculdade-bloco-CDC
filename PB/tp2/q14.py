def torres_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f'Mover disco 1 de {origem} para {destino}')
        return
    torres_hanoi(n - 1, origem, auxiliar, destino)
    print(f'Mover disco {n} de {origem} para {destino}')
    torres_hanoi(n - 1, auxiliar, destino, origem)

n_discos = 3
torres_hanoi(n_discos, 'I', 'III', 'II')
