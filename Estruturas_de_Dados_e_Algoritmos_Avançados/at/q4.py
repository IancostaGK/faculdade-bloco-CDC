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
            connectionstyle='arc3, rad = 0.1', 
            node_color="#cccccc", node_size=tamanho)
    pesos = nx.get_edge_attributes(g, "peso")
    nx.draw_networkx_edge_labels(g, pos, pesos, label_pos=0.8)
    plt.show()

  def kruskal_mst(self):
    edges = []
    for vertice in self.vertices:
      for vizinho, peso in vertice.vizinhos.items():
        edges.append((peso, vertice, vizinho))
    edges = sorted(edges, key=lambda x: x[0])  # Ordena arestas por peso

    parent = {}
    rank = {}

    def find(vertice):
      if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
      return parent[vertice]

    def union(v1, v2):
      root1 = find(v1)
      root2 = find(v2)
      if root1 != root2:
        if rank[root1] > rank[root2]:
          parent[root2] = root1
        else:
          parent[root1] = root2
          if rank[root1] == rank[root2]:
            rank[root2] += 1

    for vertice in self.vertices:
      parent[vertice] = vertice
      rank[vertice] = 0

    mst = []
    for edge in edges:
      peso, v1, v2 = edge
      if find(v1) != find(v2):
        union(v1, v2)
        mst.append(edge)
    return mst

  def desenha_mst(self, mst):
    g = nx.Graph()
    for edge in mst:
      peso, v1, v2 = edge
      g.add_edge(v1, v2, peso=peso)
    pos = nx.planar_layout(g)
    tamanho = [300 * len(str(v)) for v in g.nodes]
    nx.draw(g, pos, with_labels=True, arrows=True, 
            connectionstyle='arc3, rad = 0.1', 
            node_color="#cccccc", node_size=tamanho)
    pesos = nx.get_edge_attributes(g, "peso")
    nx.draw_networkx_edge_labels(g, pos, pesos, label_pos=0.8)
    plt.show()

# Exemplo de uso
grafo = GrafoPonderado()
v1 = grafo.cria_vertice('Reservatório 1')
v2 = grafo.cria_vertice('Reservatório 2')
v3 = grafo.cria_vertice('Reservatório 3')
v4 = grafo.cria_vertice('Reservatório 4')

grafo.adiciona_aresta(v1, v2, 10)
grafo.adiciona_aresta(v1, v3, 6)
grafo.adiciona_aresta(v1, v4, 5)
grafo.adiciona_aresta(v2, v3, 15)
grafo.adiciona_aresta(v3, v4, 4)

grafo.desenha()

mst = grafo.kruskal_mst()
grafo.desenha_mst(mst)
