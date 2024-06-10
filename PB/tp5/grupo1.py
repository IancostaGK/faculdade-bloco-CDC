import grafo 
import heap

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


def agm_prim(v_orig):
  """
  Implementa o algoritmo de Prim
  Retorna um conjunto de arestas formando uma árvore
  geradora mínima encontrada a partir de v_orig
  """
  
  def peso_aresta(aresta):
    return aresta[2]

  arestas_agm = set()
  vertices_agm = set()
  arestas = heap.Heap(chave=peso_aresta, max_heap=False)

  # Adiciona o vértice de origem na AGM
  v_atual = v_orig
  vertices_agm.add(v_atual)

  while True:
    # Verifica as arestas para vizinhos do vértice atual
    for vizinho, peso in v_atual.vizinhos.items():
      # Se o vizinho não está na AGM, insere a aresta no heap
      if vizinho not in vertices_agm:
        arestas.insere((v_atual, vizinho, peso))
    # Seleciona a aresta de menor peso no heap para um
    # vértice que não esteja na AGM
    aresta = arestas.remove()
    while not arestas.vazio() and aresta[1] in vertices_agm:
      aresta = arestas.remove()
    # Se não encontrar uma aresta, encerra
    if aresta is None or aresta[1] in vertices_agm:
      break
    # Caso contrário, insere novo vértice na AGM,
    # conectado pela aresta selecionada
    v_atual = aresta[1]
    vertices_agm.add(v_atual)
    arestas_agm.add(aresta)
  # Retorna arestas da árvore geradora mínima
  return arestas_agm

cidades = grafo.GrafoPonderado()

atlanta = cidades.cria_vertice("Atlanta")
boston = cidades.cria_vertice("Boston")
chicago = cidades.cria_vertice("Chicago")
denver = cidades.cria_vertice("Denver")
el_paso = cidades.cria_vertice("El Paso")

cidades.adiciona_aresta(atlanta, boston, 100)
cidades.adiciona_aresta(atlanta, denver, 160)
cidades.adiciona_aresta(boston, chicago, 120)
cidades.adiciona_aresta(boston, denver, 180)
cidades.adiciona_aresta(chicago, el_paso, 80)
cidades.adiciona_aresta(denver, chicago, 40)
cidades.adiciona_aresta(denver, el_paso, 140)
cidades.adiciona_aresta(el_paso, boston, 100)

print(caminho_mais_curto_dijkstra(atlanta, el_paso))
print(agm_prim(atlanta))
print(kruskal_mst(cidades))

cidades.desenha()