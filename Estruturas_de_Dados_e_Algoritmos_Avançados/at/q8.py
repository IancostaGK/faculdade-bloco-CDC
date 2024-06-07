import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class GrafoPonderado:
  def __init__(self):
    self.vertices = []
    self.arestas = {}

  def cria_vertice(self, valor):
    self.vertices.append(valor)
    self.arestas[valor] = {}
    return valor

  def adiciona_aresta(self, v1, v2, peso):
    self.arestas[v1][v2] = peso
    self.arestas[v2][v1] = peso  # Adiciona a aresta bidirecionalmente

  def floyd_warshall(self):
    n = len(self.vertices)
    dist = np.full((n, n), np.inf)
    np.fill_diagonal(dist, 0)
    vertice_idx = {vertice: idx for idx, vertice in enumerate(self.vertices)}
    
    for v1 in self.arestas:
      for v2 in self.arestas[v1]:
        i, j = vertice_idx[v1], vertice_idx[v2]
        dist[i][j] = self.arestas[v1][v2]
    
    for k in range(n):
      for i in range(n):
        for j in range(n):
          dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist, vertice_idx

  def nearest_neighbor(self, start, dist_matrix, vertice_idx):
    n = len(self.vertices)
    visited = [False] * n
    route = [start]
    total_distance = 0
    current_idx = vertice_idx[start]
    visited[current_idx] = True

    for _ in range(n - 1):
      next_idx = np.argmin([dist_matrix[current_idx][j] if not visited[j] else np.inf for j in range(n)])
      total_distance += dist_matrix[current_idx][next_idx]
      current_idx = next_idx
      route.append(self.vertices[current_idx])
      visited[current_idx] = True

    total_distance += dist_matrix[current_idx][vertice_idx[start]]
    route.append(start)
    return route, total_distance

  def melhor_rota(self):
    dist_matrix, vertice_idx = self.floyd_warshall()
    melhor_rota = None
    menor_distancia = np.inf

    for vertice in self.vertices:
      rota, distancia = self.nearest_neighbor(vertice, dist_matrix, vertice_idx)
      if distancia < menor_distancia:
        melhor_rota = rota
        menor_distancia = distancia

    return melhor_rota, menor_distancia

  def desenha(self, caminho=[]):
    g = nx.Graph()
    for vertice in self.vertices:
      g.add_node(vertice)
    for v1 in self.arestas:
      for v2, peso in self.arestas[v1].items():
        g.add_edge(v1, v2, weight=peso)
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, arrows=True, node_color="#cccccc")
    pesos = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=pesos, label_pos=0.3)
    if caminho:
      edge_list = [(caminho[i], caminho[i + 1]) for i in range(len(caminho) - 1)]
      nx.draw_networkx_edges(g, pos, edgelist=edge_list, edge_color='r', width=2)
    plt.show()

# Exemplo de uso
grafo = GrafoPonderado()
v1 = grafo.cria_vertice('1')
v2 = grafo.cria_vertice('2')
v3 = grafo.cria_vertice('3')
v4 = grafo.cria_vertice('4')
v5 = grafo.cria_vertice('5')
v6 = grafo.cria_vertice('6')
v7 = grafo.cria_vertice('7')
v8 = grafo.cria_vertice('8')
v9 = grafo.cria_vertice('9')
v10 = grafo.cria_vertice('10')
v11 = grafo.cria_vertice('11')
vm = grafo.cria_vertice('M')

grafo.adiciona_aresta(v1, v2, 4) 
grafo.adiciona_aresta(v1, v5, 5)
grafo.adiciona_aresta(v2, v5, 4)
grafo.adiciona_aresta(v2, vm, 3)
grafo.adiciona_aresta(vm, v5, 6)
grafo.adiciona_aresta(vm, v3, 4)
grafo.adiciona_aresta(v3, v4, 5)  
grafo.adiciona_aresta(v3, v10, 3)  
grafo.adiciona_aresta(v3, v8, 5) 
grafo.adiciona_aresta(v4, v10, 4) 
grafo.adiciona_aresta(v5, v6, 2) 
grafo.adiciona_aresta(v5, v8, 5) 
grafo.adiciona_aresta(v6, v8, 4) 
grafo.adiciona_aresta(v6, v7, 4) 
grafo.adiciona_aresta(v8, v7, 3) 
grafo.adiciona_aresta(v9, v7, 4) 
grafo.adiciona_aresta(v9, v11, 3) 
grafo.adiciona_aresta(v10, v11, 3) 
grafo.adiciona_aresta(v8, v10, 3) 

dist_matrix, vertice_idx = grafo.floyd_warshall()
print("Matriz de Floyd-Warshall (tempo total para percorrer cada caminho):")
print(dist_matrix)

rota, distancia = grafo.melhor_rota()
print(f"Melhor rota encontrada: {rota}, distância total: {distancia}")

grafo.desenha(rota)
