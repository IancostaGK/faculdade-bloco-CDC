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

  def agm_prim(self):
    if not self.vertices:
      return set()

    arestas_agm = set()
    vertices_agm = set()
    arestas = []
    v_inicial = self.vertices[0]
    vertices_agm.add(v_inicial)

    for vizinho, peso in v_inicial.vizinhos.items():
      heapq.heappush(arestas, (peso, v_inicial, vizinho))

    while arestas:
      peso, v1, v2 = heapq.heappop(arestas)
      if v2 not in vertices_agm:
        vertices_agm.add(v2)
        arestas_agm.add((v1, v2, peso))
        for vizinho, peso in v2.vizinhos.items():
          if vizinho not in vertices_agm:
            heapq.heappush(arestas, (peso, v2, vizinho))

    return arestas_agm

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

def galpoes_guloso(grafo):
  arestas = [(v1, v2) for v1 in grafo.vertices for v2 in v1.vizinhos]
  galpoes = set()
  cobertos = set()

  while cobertos != set(arestas):
    max_cobertura = 0
    melhor_vertice = None

    for vertice in grafo.vertices:
      cobertura = sum(1 for (v1, v2) in arestas if v1 == vertice or v2 == vertice)
      if cobertura > max_cobertura and vertice not in galpoes:
        max_cobertura = cobertura
        melhor_vertice = vertice

    galpoes.add(melhor_vertice)
    cobertos.update((v1, v2) for (v1, v2) in arestas if v1 == melhor_vertice or v2 == melhor_vertice)

  return galpoes

grafo = GrafoPonderado()
v0 = grafo.cria_vertice('Blum')
v1 = grafo.cria_vertice('Cerf')
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

# Encontrar o caminho mais rápido de Blum a Naur
inicio = v0 
fim = v3
caminho, distancia_total = dijkstra(grafo, inicio, fim)
print("Caminho mais rápido de Blum a Naur:", caminho)
print("Tempo total:", distancia_total, "minutos")

# Encontrar o caminho mais rápido para percorrer todas as cidades e retornar a Blum
caminho, distancia_total = caminho_mais_curto_todas_cidades(grafo, inicio)
print("Caminho mais rápido para percorrer todas as cidades e retornar a Blum:", caminho)
print("Tempo total:", distancia_total, "minutos")

# Encontrar a árvore geradora mínima (AGM) usando Prim
arestas_agm = grafo.agm_prim()
print("Arestas na árvore geradora mínima:")
for aresta in arestas_agm:
  print(f"{aresta[0]} -- {aresta[1]}: {aresta[2]} minutos")

# Determinar as cidades onde serão instalados os galpões
galpoes = galpoes_guloso(grafo)
print("Cidades onde serão instalados os galpões:")
for galpao in galpoes:
  print(galpao)

grafo.desenha()