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

def componentes_conexas(grafo, altitude_limite=float('inf')):
  rotulos = {v: v for v in grafo.vertices}
  
  alterou = True
  while alterou:
    alterou = False
    for vertice in grafo.vertices:
      for vizinho, peso in vertice.vizinhos.items():
        if peso <= altitude_limite:
          if rotulos[vertice] != rotulos[vizinho]:
            rotulo_maior = max(rotulos[vertice], rotulos[vizinho], key=lambda v: str(v))
            rotulo_menor = min(rotulos[vertice], rotulos[vizinho], key=lambda v: str(v))
            for v in rotulos:
              if rotulos[v] == rotulo_maior:
                rotulos[v] = rotulo_menor
            alterou = True
  return [rotulos[v].valor for v in grafo.vertices] 

def vertices_componente(rotulos):
  componentes = {}
  for i, rotulo in enumerate(rotulos):
    if rotulo not in componentes:
      componentes[rotulo] = []
    componentes[rotulo].append(i)
  return componentes

# # Exemplo de uso
grafo = GrafoPonderado()
v0 = grafo.cria_vertice('Blum')
v1 = grafo.cria_vertice('Cerl')
v2 = grafo.cria_vertice('Gray')
v3 = grafo.cria_vertice('Naur')
v4 = grafo.cria_vertice('Kay')
v5 = grafo.cria_vertice('Dahi')

grafo.adiciona_aresta(v0, v1, 18)
grafo.adiciona_aresta(v0, v5, 19)
grafo.adiciona_aresta(v1, v2, 28)
grafo.adiciona_aresta(v1, v3, 51)
grafo.adiciona_aresta(v1, v4, 29)
grafo.adiciona_aresta(v1, v5, 17)
grafo.adiciona_aresta(v2, v3, 24)
grafo.adiciona_aresta(v2, v4, 11)
grafo.adiciona_aresta(v2, v5, 26)
grafo.adiciona_aresta(v3, v4, 20)
grafo.adiciona_aresta(v4, v5, 31)

grafo.desenha()

# Testando a função com diferentes altitudes
altitudes = [50, 21, 15]
for altitude in altitudes:
  rotulos = componentes_conexas(grafo, altitude)
  componentes = vertices_componente(rotulos)
  print(f"Altitude limite: {altitude}")
  print("Rótulos:", rotulos)
  print("Componentes conexas:", componentes)
  print()
