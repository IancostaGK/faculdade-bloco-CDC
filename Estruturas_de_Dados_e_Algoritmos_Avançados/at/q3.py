import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Vertice(object):
  def __init__(self, valor):
    self.valor = valor
    self.vizinhos = []

  def __repr__(self):
    return str(self.valor)

class Grafo(object):
  def __init__(self, direcionado=False):
    self.vertices = []
    self.direcionado = direcionado

  def cria_vertice(self, valor):
    vertice = Vertice(valor)
    self.vertices.append(vertice)
    return vertice

  def adiciona_aresta(self, v1, v2):
    v1.vizinhos.append(v2)
    if not self.direcionado:
      v2.vizinhos.append(v1)

  def desenha(self):
    g = nx.DiGraph() if self.direcionado else nx.Graph()
    for vertice in self.vertices:
      g.add_node(vertice)
      for vizinho in vertice.vizinhos:
        g.add_edge(vertice, vizinho)
    pos = nx.planar_layout(g)
    tamanho = [300 * len(str(v)) for v in g.nodes]
    nx.draw(g, pos, with_labels=True, arrows=True, 
      connectionstyle='arc3, rad = 0.1', 
      node_color="#cccccc", node_size=tamanho)
    plt.show()

  def travessia_dfs(self, v_orig, visitados=None):
    if not visitados:
      visitados = set()
    visitados.add(v_orig)
    for vizinho in v_orig.vizinhos:
      if vizinho not in visitados:
        self.travessia_dfs(vizinho, visitados)
    return visitados

  def busca_dfs(self, v_orig, v_dest, visitados=None):
    if v_orig == v_dest or v_dest in v_orig.vizinhos:
      return True
    if not visitados:
      visitados = set()
    visitados.add(v_orig)
    for vizinho in v_orig.vizinhos:
      if vizinho not in visitados and self.busca_dfs(vizinho, v_dest, visitados):
        return True
    return False

  def travessia_bfs(self, v_orig):
    visitados = set()
    fila = deque([v_orig])
    while fila:
      vertice = fila.popleft()
      if vertice not in visitados:
        visitados.add(vertice)
        fila.extend(v for v in vertice.vizinhos if v not in visitados)
    return visitados

# Create a graph of each type with the vertices A, B, C, D, E, F, G, H, I, and J, and the edges A-G, A-I, C-F, D-A, D-I, H-D, H-E, H-F, H-G, I-H, J-C, and J-H.
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
arestas = [('A', 'G'), ('A', 'I'), ('C', 'F'), ('D', 'A'), ('D', 'I'), ('H', 'D'), ('H', 'E'), ('H', 'F'), ('H', 'G'), ('I', 'H'), ('J', 'C'), ('J', 'H')]

for direcionado in [False, True]:
  grafo = Grafo(direcionado)
  vertice_dict = {v: grafo.cria_vertice(v) for v in vertices}
  for v1, v2 in arestas:
    grafo.adiciona_aresta(vertice_dict[v1], vertice_dict[v2])

  print(f"{'Directed' if direcionado else 'Undirected'} Graph:")
  print("DFS from J:", grafo.travessia_dfs(vertice_dict['J']))
  print("BFS from C:", grafo.travessia_bfs(vertice_dict['C']))
  print("DFS from J to I:", grafo.busca_dfs(vertice_dict['J'], vertice_dict['I']))
  grafo.desenha()
