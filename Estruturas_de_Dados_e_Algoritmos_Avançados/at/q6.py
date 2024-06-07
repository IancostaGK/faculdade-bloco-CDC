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

def dijkstra(grafo, inicio, fim):
  distancias = {vertice: float('infinity') for vertice in grafo.vertices}
  distancias[inicio] = 0
  caminho = {vertice: None for vertice in grafo.vertices}
  pq = [(0, inicio)]
  
  while pq:
    (distancia_atual, vertice_atual) = heapq.heappop(pq)
    
    if distancia_atual > distancias[vertice_atual]:
      continue
    
    for vizinho, peso in vertice_atual.vizinhos.items():
      distancia = distancia_atual + peso
      
      if distancia < distancias[vizinho]:
        distancias[vizinho] = distancia
        caminho[vizinho] = vertice_atual
        heapq.heappush(pq, (distancia, vizinho))
  
  caminho_reverso = []
  vertice_atual = fim
  while vertice_atual is not None:
    caminho_reverso.append(vertice_atual)
    vertice_atual = caminho[vertice_atual]
  caminho_reverso.reverse()
  
  return caminho_reverso, distancias[fim]

def caminho_mais_curto_todas_cidades(grafo, inicio):
  vertices = grafo.vertices[:]
  vertices.remove(inicio)
  menor_caminho = None
  menor_distancia = float('infinity')
  
  for perm in permutations(vertices):
    distancia_total = 0
    caminho_atual = [inicio]
    vertice_atual = inicio
    
    for proximo_vertice in perm:
      _, distancia = dijkstra(grafo, vertice_atual, proximo_vertice)
      distancia_total += distancia
      vertice_atual = proximo_vertice
      caminho_atual.append(proximo_vertice)
    
    _, distancia = dijkstra(grafo, vertice_atual, inicio)
    distancia_total += distancia
    caminho_atual.append(inicio)
    
    if distancia_total < menor_distancia:
      menor_distancia = distancia_total
      menor_caminho = caminho_atual
  
  return menor_caminho, menor_distancia

def prim(grafo):
  mst = GrafoPonderado()
  visitados = set()
  pq = []
  
  vertice_inicial = grafo.vertices[0]
  visitados.add(vertice_inicial)
  for vizinho, peso in vertice_inicial.vizinhos.items():
    heapq.heappush(pq, (peso, vertice_inicial, vizinho))
  
  while pq:
    peso, v1, v2 = heapq.heappop(pq)
    if v2 not in visitados:
      visitados.add(v2)
      mst.adiciona_aresta(v1, v2, peso)
      for vizinho, peso in v2.vizinhos.items():
        if vizinho not in visitados:
          heapq.heappush(pq, (peso, v2, vizinho))
  
  return mst

def instala_galpoes(grafo):
  cobertos = set()
  galpoes = set()
  
  while len(cobertos) < len(grafo.vertices):
    melhor_vertice = None
    maior_cobertura = 0
    
    for vertice in grafo.vertices:
      if vertice not in galpoes:
        cobertura = sum(1 for vizinho in vertice.vizinhos if vizinho not in cobertos)
        if cobertura > maior_cobertura:
          maior_cobertura = cobertura
          melhor_vertice = vertice
    
    galpoes.add(melhor_vertice)
    cobertos.add(melhor_vertice)
    for vizinho in melhor_vertice.vizinhos:
      cobertos.add(vizinho)
  
  return galpoes

# Exemplo de uso
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

# # Desenhar o grafo
# grafo.desenha()

# Encontrar o caminho mais rápido de Blum a Naur
inicio = v0  # Blum
fim = v3  # Naur
caminho, distancia_total = dijkstra(grafo, inicio, fim)
print("Caminho mais rápido de Blum a Naur:", caminho)
print("Tempo total:", distancia_total, "minutos")

# Encontrar o caminho mais rápido para percorrer todas as cidades e retornar a Blum
caminho, distancia_total = caminho_mais_curto_todas_cidades(grafo, inicio)
print("Caminho mais rápido para percorrer todas as cidades e retornar a Blum:", caminho)
print("Tempo total:", distancia_total, "minutos")

# Encontrar a MST usando o algoritmo de Prim
mst = prim(grafo)
print("Ferrovias a serem mantidas para minimizar o tempo total:")
for vertice in mst.vertices:
  for vizinho, peso in vertice.vizinhos.items():
    print(f"{vertice} - {vizinho}: {peso} minutos")

# Encontrar as cidades onde serão instalados os galpões
galpoes = instala_galpoes(grafo)
print("Cidades onde serão instalados os galpões:", [str(g) for g in galpoes])
