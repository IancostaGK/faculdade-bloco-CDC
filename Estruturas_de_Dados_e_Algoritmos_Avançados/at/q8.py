import matplotlib.pyplot as plt
import networkx as nx
import heapq
from itertools import permutations

class VerticeGrafoPonderado:
  def __init__(self, valor):
    self.valor = valor
    self.vizinhos = {}

  def __repr__(self):
    return str(self.valor)

class GrafoPonderado:
  def __init__(self):
    self.vertices = []

  def cria_vertice(self, valor):
    vertice = VerticeGrafoPonderado(valor)
    self.vertices.append(vertice)
    return vertice

  def adiciona_aresta(self, v1, v2, peso=1):
    v1.vizinhos[v2] = peso
    v2.vizinhos[v1] = peso  # Adiciona a aresta bidirecionalmente

  def desenha(self):
    g = nx.Graph()
    for vertice in self.vertices:
      g.add_node(vertice)
      for vizinho, peso in vertice.vizinhos.items():
        g.add_edge(vertice, vizinho, peso=peso)
    pos = nx.spring_layout(g)
    tamanho = [300 * len(str(v)) for v in g.nodes]
    nx.draw(g, pos, with_labels=True, arrows=True, 
            node_color="#cccccc", node_size=tamanho)
    pesos = nx.get_edge_attributes(g, "peso")
    nx.draw_networkx_edge_labels(g, pos, pesos, label_pos=0.8)
    plt.show()


# Exemplo de uso
grafo = GrafoPonderado()
v1 = grafo.cria_vertice('1')
v2 = grafo.cria_vertice('2')
v3 = grafo.cria_vertice('3')
v4 = grafo.cria_vertice('4')
v5 = grafo.cria_vertice('5')
v6 = grafo.cria_vertice('6')
v7 = grafo.cria_vertice('7')
v8 = grafo.cria_vertice('8')
v9 = grafo.cria_vertice('9')
v10 = grafo.cria_vertice('10')
v11 = grafo.cria_vertice('11')
vm = grafo.cria_vertice('M')

grafo.adiciona_aresta(v1, v2, 4) 
grafo.adiciona_aresta(v1, v5, 5)
grafo.adiciona_aresta(v2, v5, 4)
grafo.adiciona_aresta(v2, vm, 3)
grafo.adiciona_aresta(vm, v5, 6)
grafo.adiciona_aresta(vm, v3, 4)
grafo.adiciona_aresta(v3, v4, 5)  
grafo.adiciona_aresta(v3, v10, 3)  
grafo.adiciona_aresta(v3, v8, 5) 
grafo.adiciona_aresta(v4, v10, 4) 
grafo.adiciona_aresta(v5, v6, 2) 
grafo.adiciona_aresta(v5, v8, 5) 
grafo.adiciona_aresta(v6, v8, 4) 
grafo.adiciona_aresta(v6, v7, 4) 
grafo.adiciona_aresta(v8, v7, 3) 
grafo.adiciona_aresta(v9, v7, 4) 
grafo.adiciona_aresta(v9, v11, 3) 
grafo.adiciona_aresta(v10, v11, 3) 
grafo.adiciona_aresta(v8, v10, 3) 

# Desenhar o grafo
grafo.desenha()

