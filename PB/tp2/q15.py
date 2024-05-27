class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def travessia_pre_ordem(raiz):
    if raiz is not None:
        print(raiz.valor, end=' ')
        travessia_pre_ordem(raiz.esquerda)
        travessia_pre_ordem(raiz.direita)

def travessia_pos_ordem(raiz):
    if raiz is not None:
        travessia_pos_ordem(raiz.esquerda)
        travessia_pos_ordem(raiz.direita)
        print(raiz.valor, end=' ')

def travessia_em_ordem(raiz):
    if raiz is not None:
        travessia_em_ordem(raiz.esquerda)
        print(raiz.valor, end=' ')
        travessia_em_ordem(raiz.direita)

raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)

print("Travessia em Pré-ordem:")
travessia_pre_ordem(raiz)
print("\nTravessia em Pós-ordem:")
travessia_pos_ordem(raiz)
print("\nTravessia em Ordem Simétrica:")
travessia_em_ordem(raiz)
