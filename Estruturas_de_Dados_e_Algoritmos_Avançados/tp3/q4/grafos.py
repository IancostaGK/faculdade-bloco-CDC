import matplotlib.pyplot as plt
import networkx as nx


def travessia_dfs(v_orig, visitados=None):
  """
  Implementa travessia de grafo baseada no 
  algoritmo de busca em profundidade (DFS)
  
  Retorna conjunto de vértices visitados
  """
  if not visitados:
    visitados = set()
  visitados.add(v_orig)
  for vizinho in v_orig.vizinhos:
    if vizinho not in visitados:
      travessia_dfs(vizinho, visitados)
  return visitados


def busca_dfs(v_orig, v_dest, 
              visitados=None):
  """
  Implementa busca em grafo baseada no 
  algoritmo de busca em profundidade (DFS)
  
  Retorna True (se encontrar um caminho de 
  v_orig a v_dest) ou False (caso contrário)
  """
  if (v_orig == v_dest or 
      v_dest in v_orig.vizinhos):
    return True
  if not visitados:
    visitados = set()
  visitados.add(v_orig)
  for vizinho in v_orig.vizinhos:
    if (vizinho not in visitados and 
        busca_dfs(vizinho, v_dest, 
                  visitados)):
      return True
  return False


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