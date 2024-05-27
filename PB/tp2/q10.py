class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserir(self, valor):
        novo_no = No(valor)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def remover(self, valor):
        atual = self.primeiro
        anterior = None
        while atual:
            if atual.valor == valor:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.primeiro = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def buscar(self, valor):
        atual = self.primeiro
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def imprimir(self):
        atual = self.primeiro
        while atual:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print()

    def ordenar(self):
        elementos = []
        atual = self.primeiro
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        elementos.sort()
        self.primeiro = None
        for elemento in elementos:
            self.inserir(elemento)

lista = ListaEncadeada()
lista.inserir(3)
lista.inserir(1)
lista.inserir(2)
lista.imprimir()  
lista.ordenar()
lista.imprimir()  
lista.remover(2)
lista.imprimir() 
