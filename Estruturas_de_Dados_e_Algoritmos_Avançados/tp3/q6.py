import matplotlib.pyplot as plt
import networkx as nx

def caminho_mais_curto(grafo, inicio, fim):
	fila = [(inicio, [inicio])]
	while fila:
		vertice, caminho = fila.pop(0)
		for proximo in set(grafo.vertices[grafo.vertices.index(vertice)].vizinhos) - set(caminho):
			if proximo == fim:
				return caminho + [proximo]
			else:
				fila.append((proximo, caminho + [proximo]))
	return []

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
    
amigos = Grafo()

idris = amigos.cria_vertice("Idris")
talia = amigos.cria_vertice("Talia")
ken = amigos.cria_vertice("Ken")
marco = amigos.cria_vertice("Marco")
sasha = amigos.cria_vertice("Sasha")
lina = amigos.cria_vertice("Lina")
Kamil = amigos.cria_vertice("Kamil")

amigos.adiciona_aresta(idris, talia)
amigos.adiciona_aresta(talia, ken)
amigos.adiciona_aresta(ken, marco)
amigos.adiciona_aresta(marco, sasha)
amigos.adiciona_aresta(sasha, lina)
amigos.adiciona_aresta(lina, Kamil)
amigos.adiciona_aresta(Kamil, idris)

caminho = caminho_mais_curto(amigos, idris, lina)
print(caminho)
caminho = caminho_mais_curto(amigos, idris, ken)
print(caminho)
caminho = caminho_mais_curto(amigos, idris, marco)
print(caminho)
caminho = caminho_mais_curto(amigos, idris, sasha)
print(caminho)

amigos.desenha()