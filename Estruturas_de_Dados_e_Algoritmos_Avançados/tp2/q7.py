class GrafoMatrizAdjacencia:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz = [[0] * len(vertices) for _ in range(len(vertices))]

    def adiciona_aresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            idx1 = self.vertices.index(v1)
            idx2 = self.vertices.index(v2)
            self.matriz[idx1][idx2] = 1
            self.matriz[idx2][idx1] = 1

    def imprime_pares_relacionados(self):
        for i in range(len(self.vertices)):
            for j in range(i + 1, len(self.vertices)):
                if self.matriz[i][j] == 1:
                    print(f"({self.vertices[i]}, {self.vertices[j]})")

vertices = ["broca", "martelo", "serra", "faca", "colher", "garfo", "pregos", 
            "alfinetes", "agulhas", "esmalte", "sombra", "escova", "oculos"]
grafo = GrafoMatrizAdjacencia(vertices)

arestas = {
    "broca": ['martelo'],
    "martelo": ['broca', 'serra', "pregos"],
    "serra": ['martelo', 'faca'],
    "faca": ['serra', "colher", "garfo"],
    "colher": ['faca'],
    "garfo": ['faca'],
    "pregos": ['martelo', 'alfinetes', 'agulhas', 'esmalte'],
    "alfinetes": ['pregos', 'agulhas'],
    "agulhas": ['pregos', 'alfinetes'],
    "esmalte": ['pregos', 'sombra', 'escova'],
    "sombra": ['esmalte', 'oculos'],
    "escova": ['esmalte'],
    "oculos": ['sombra']
}

for v1, vizinhos in arestas.items():
    for v2 in vizinhos:
        grafo.adiciona_aresta(v1, v2)

grafo.imprime_pares_relacionados()
