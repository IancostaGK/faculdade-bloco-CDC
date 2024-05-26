from collections import deque

class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].append(destino)

    def dfs(self, vertice_inicial):
        visitados = set()
        self._dfs_recursive(vertice_inicial, visitados)

    def _dfs_recursive(self, vertice, visitados):
        visitados.add(vertice)
        print(vertice, end=' ')

        for vizinho in self.vertices[vertice]:
            if vizinho not in visitados:
                self._dfs_recursive(vizinho, visitados)

    def bfs(self, vertice_inicial):
        visitados = set()
        fila = deque([vertice_inicial])

        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                print(vertice, end=' ')
                visitados.add(vertice)
                for vizinho in self.vertices[vertice]:
                    fila.append(vizinho)

    def encontrar_saida_labirinto_dfs(self, vertice_inicial, vertice_saida):
        visitados = set()
        caminho = []
        self._encontrar_saida_labirinto_dfs_recursive(vertice_inicial, vertice_saida, visitados, caminho)
        return caminho

    def _encontrar_saida_labirinto_dfs_recursive(self, vertice_atual, vertice_saida, visitados, caminho):
        visitados.add(vertice_atual)
        caminho.append(vertice_atual)

        if vertice_atual == vertice_saida:
            return True

        for vizinho in self.vertices[vertice_atual]:
            if vizinho not in visitados:
                if self._encontrar_saida_labirinto_dfs_recursive(vizinho, vertice_saida, visitados, caminho):
                    return True

        caminho.pop()
        return False

    def encontrar_saida_labirinto_bfs(self, vertice_inicial, vertice_saida):
        fila = deque([(vertice_inicial, [vertice_inicial])])
        visitados = set([vertice_inicial])

        while fila:
            vertice, caminho = fila.popleft()

            if vertice == vertice_saida:
                return caminho

            for vizinho in self.vertices[vertice]:
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho]))
                    visitados.add(vizinho)

        return None

    def visualizar_labirinto(self):
        for vertice, vizinhos in self.vertices.items():
            print(f"{vertice} -> {', '.join(vizinhos)}")

labirinto = Grafo()
# Adicionando vértices e arestas para representar o labirinto

labirinto.adicionar_vertice('A')
labirinto.adicionar_vertice('B')
labirinto.adicionar_vertice('C')
labirinto.adicionar_vertice('D')
labirinto.adicionar_vertice('E')
labirinto.adicionar_vertice('F')
labirinto.adicionar_vertice('G')
labirinto.adicionar_vertice('H')
labirinto.adicionar_vertice('I')
labirinto.adicionar_vertice('J')
labirinto.adicionar_vertice('K')
labirinto.adicionar_vertice('L')
labirinto.adicionar_vertice('M')
labirinto.adicionar_vertice('N')
labirinto.adicionar_vertice('O')
labirinto.adicionar_vertice('P')

# Adicionando arestas
labirinto.adicionar_aresta('A', 'B')
labirinto.adicionar_aresta('A', 'C')
labirinto.adicionar_aresta('B', 'D')
labirinto.adicionar_aresta('C', 'E')
labirinto.adicionar_aresta('D', 'F')
labirinto.adicionar_aresta('E', 'F')
labirinto.adicionar_aresta('E', 'G')
labirinto.adicionar_aresta('F', 'H')
labirinto.adicionar_aresta('G', 'I')
labirinto.adicionar_aresta('H', 'J')
labirinto.adicionar_aresta('I', 'K')
labirinto.adicionar_aresta('J', 'L')
labirinto.adicionar_aresta('K', 'M')
labirinto.adicionar_aresta('L', 'N')
labirinto.adicionar_aresta('M', 'O')
labirinto.adicionar_aresta('N', 'P')

print("DFS:")
labirinto.dfs('A')
print("\nBFS:")
labirinto.bfs('A')

print("\nCaminho para sair do labirinto (DFS):", labirinto.encontrar_saida_labirinto_dfs('A', 'P'))
print("Caminho para sair do labirinto (BFS):", labirinto.encontrar_saida_labirinto_bfs('A', 'O'))

labirinto.visualizar_labirinto()
