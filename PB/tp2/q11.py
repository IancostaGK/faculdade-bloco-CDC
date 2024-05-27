class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.tamanho = 0
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.tamanho == 0

    def esta_cheia(self):
        return self.tamanho == self.capacidade

    def enfileirar(self, valor):
        if self.esta_cheia():
            print("A fila está cheia. Não é possível enfileirar.")
            return False

        novo_no = No(valor)
        if self.esta_vazia():
            self.inicio = novo_no
        else:
            self.fim.proximo = novo_no
        self.fim = novo_no
        self.fim.proximo = self.inicio
        self.tamanho += 1
        return True

    def desenfileirar(self):
        if self.esta_vazia():
            print("A fila está vazia. Não é possível desenfileirar.")
            return None

        valor_removido = self.inicio.valor
        if self.tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.fim.proximo = self.inicio
        self.tamanho -= 1
        return valor_removido

    def frente(self):
        if self.esta_vazia():
            print("A fila está vazia.")
            return None
        return self.inicio.valor

    def imprimir(self):
        if self.esta_vazia():
            print("A fila está vazia.")
            return

        atual = self.inicio
        while atual.proximo != self.inicio:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print(atual.valor)

fila = FilaCircular(5)
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.imprimir()
fila.desenfileirar()
fila.imprimir()
print(fila.frente())
fila.enfileirar(4)
fila.enfileirar(5)
fila.enfileirar(6)
fila.imprimir()
fila.desenfileirar()
fila.imprimir()
