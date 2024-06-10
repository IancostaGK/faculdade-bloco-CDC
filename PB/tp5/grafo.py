import matplotlib.pyplot as plt
import networkx as nx

def caminho_mais_curto_dijkstra(v_orig, v_dest):
  """
  Implementa o algoritmo de Dijkstra
  Retorna o caminho mais curto entre v_orig e v_dest
  """
  
  menor_peso = {}
  predecessor = {}
  visitados = set()
  
  menor_peso[v_orig] = 0
  v_atual = v_orig
  
  while v_atual:
    # Visita o vértice atual
    visitados.add(v_atual)
    # Verifica as arestas para seus vizinhos
    for vizinho, peso in v_atual.vizinhos.items():
      # Calcula peso total do caminho de 
      # v_orig a vizinho via v_atual
      peso_total = menor_peso[v_atual] + peso
      # Se for o caminho mais curto (até o momento)
      # de v_orig a vizinho, atualiza as tabelas
      if (vizinho not in menor_peso or 
          peso_total < menor_peso[vizinho]):
        menor_peso[vizinho] = peso_total
        predecessor[vizinho] = v_atual
    # Seleciona o vértice não visitado com
    # menor valor na tabela de pesos
    v_atual = None
    for v in menor_peso:
      if (v not in visitados and 
          (not v_atual or menor_peso[v] < menor_peso[v_atual])):
        v_atual = v
  # Reconstrói e retorna o caminho mais curto
  caminho = []
  v_atual = v_dest
  while v_atual != v_orig:
    caminho.append(v_atual)
    v_atual = predecessor[v_atual]
  caminho.append(v_orig)
  caminho.reverse()
  return caminho


class Vertice(object):
  """Implementa um vértice de grafo"""

  def __init__(self, valor):
    self.valor = valor
    self.vizinhos = []

  def __repr__(self):
    return str(self.valor)


class VerticeGrafoPonderado(Vertice):
  """Implementa um vértice de grafo ponderado"""

  def __init__(self, valor):
    self.valor = valor
    self.vizinhos = {}


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

class GrafoPonderado(Grafo):
  """Implementa um grafo ponderado"""

  def cria_vertice(self, valor):
    """Cria vértice com o valor definido"""
    vertice = VerticeGrafoPonderado(valor)
    self.vertices.append(vertice)
    return vertice

  def adiciona_aresta(self, v1, v2, peso=1.0):
    """Adiciona aresta entre v1 e v2 com peso"""
    v1.vizinhos[v2] = peso
    v2.vizinhos[v1] = peso

  def desenha(self, arestas_destacadas=None):
    """Desenha o grafo"""
    g = nx.Graph()
    for vertice in self.vertices:
      g.add_node(vertice)
      for vizinho, peso in vertice.vizinhos.items():
        cor = ("#000000" if arestas_destacadas is None or 
                            (vertice, vizinho) in arestas_destacadas or
                            (vizinho, vertice) in arestas_destacadas 
               else "#cccccc")
        g.add_edge(vertice, vizinho, peso=peso, cor=cor)
    pos = nx.planar_layout(g)
    tamanho = [300 * len(str(v)) for v in g.nodes]
    cores = nx.get_edge_attributes(g, "cor")
    nx.draw(g, pos, with_labels=True, arrows=True, 
            node_color="#cccccc", node_size=tamanho, 
            edge_color=cores.values())
    pesos = nx.get_edge_attributes(g, "peso")
    nx.draw_networkx_edge_labels(g, pos, pesos)
    for e in g.edges():
      nx.draw_networkx_edge_labels(g, pos, edge_labels={e: pesos[e]}, font_color=cores[e])
    plt.show()

