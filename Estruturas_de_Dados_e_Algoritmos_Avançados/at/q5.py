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
    pos = nx.planar_layout(g)
    tamanho = [300 * len(str(v)) for v in g.nodes]
    nx.draw(g, pos, with_labels=True, arrows=True, 
            node_color="#cccccc", node_size=tamanho)
    pesos = nx.get_edge_attributes(g, "peso")
    nx.draw_networkx_edge_labels(g, pos, pesos, label_pos=0.8)
    plt.show()

# Exemplo de uso
grafo = GrafoPonderado()
v1 = grafo.cria_vertice('Blum')
v2 = grafo.cria_vertice('Cerl')
v3 = grafo.cria_vertice('Gray')
v4 = grafo.cria_vertice('Naur')
v5 = grafo.cria_vertice('Kay')
v6 = grafo.cria_vertice('Dahi')

grafo.adiciona_aresta(v1, v2, 18)
grafo.adiciona_aresta(v1, v6, 19)
grafo.adiciona_aresta(v2, v3, 28)
grafo.adiciona_aresta(v2, v4, 51)
grafo.adiciona_aresta(v2, v5, 29)
grafo.adiciona_aresta(v2, v6, 17)
grafo.adiciona_aresta(v3, v4, 24)
grafo.adiciona_aresta(v3, v5, 11)
grafo.adiciona_aresta(v3, v6, 26)
grafo.adiciona_aresta(v4, v5, 20)
grafo.adiciona_aresta(v5, v6, 31)

grafo.desenha()

