import matplotlib.pyplot as plt
import networkx as nx

from fila import Fila


def travessia_bfs(v_orig):
  """
  Implementa travessia de grafo baseada no 
  algoritmo de busca em largura (BFS)

  Retorna conjunto de vértices visitados
  """
  fila = Fila()
  visitados = set()
  visitados.add(v_orig)
  fila.enfileira(v_orig)
  while not fila.vazia():
    vertice_atual = fila.desenfileira()
    for vizinho in vertice_atual.vizinhos:
      if vizinho not in visitados:
        visitados.add(vizinho)
        fila.enfileira(vizinho)
  return visitados


class Vertice(object):
  """Implementa um vértice de grafo"""

  def __init__(self, valor):
    self.valor = valor
    self.vizinhos = []

  def __repr__(self):
    return str(self.valor)


class Grafo(object):
  """Implementa um grafo simples"""

  def __init__(self):
    self.vertices = []

  def cria_vertice(self, valor):
    """Cria vértice com o valor definido"""
    vertice = Vertice(valor)
    self.vertices.append(vertice)
    return vertice

  def adiciona_aresta(self, v1, v2):
    """Adiciona aresta entre v1 e v2"""
    v1.vizinhos.append(v2)
    v2.vizinhos.append(v1)

  def desenha(self):
    """Desenha o grafo"""
    g = nx.Graph()
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

  def busca_caminho_bfs(self, origem, destino):
    """
    Verifica se existe um caminho entre origem e destino no grafo
    usando busca em largura (BFS).
    Retorna True se houver caminho, False caso contrário.
    """
    fila = Fila()
    visitados = set()
    visitados.add(origem)
    fila.enfileira(origem)
    while not fila.vazia():
      vertice_atual = fila.desenfileira()
      if vertice_atual == destino:
        return True  # Caminho encontrado
      for vizinho in vertice_atual.vizinhos:
        if vizinho not in visitados:
          visitados.add(vizinho)
          fila.enfileira(vizinho)
    return False  # Não há caminho entre origem e destino


class GrafoDirecionado(Grafo):
  """Implementa um grafo direcionado"""

  def adiciona_aresta(self, v1, v2):
    """Adiciona aresta entre v1 e v2"""
    v1.vizinhos.append(v2)

  def desenha(self):
    """Desenha o grafo"""
    g = nx.DiGraph()
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