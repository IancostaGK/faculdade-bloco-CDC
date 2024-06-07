import matplotlib.pyplot as plt
import networkx as nx

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

# # Exemplo de uso
grafo = GrafoPonderado()
v0 = grafo.cria_vertice('Blum')
v1 = grafo.cria_vertice('Cerl')
v2 = grafo.cria_vertice('Gray')
v3 = grafo.cria_vertice('Naur')
v4 = grafo.cria_vertice('Kay')
v5 = grafo.cria_vertice('Dahi')

grafo.adiciona_aresta(v0, v1, 22)
grafo.adiciona_aresta(v0, v5, 16)
grafo.adiciona_aresta(v1, v2, 34)
grafo.adiciona_aresta(v1, v3, 65)
grafo.adiciona_aresta(v1, v4, 26)
grafo.adiciona_aresta(v1, v5, 29)
grafo.adiciona_aresta(v2, v3, 30)
grafo.adiciona_aresta(v2, v4, 25)
grafo.adiciona_aresta(v2, v5, 28)
grafo.adiciona_aresta(v3, v4, 36)
grafo.adiciona_aresta(v4, v5, 24)

grafo.desenha()
