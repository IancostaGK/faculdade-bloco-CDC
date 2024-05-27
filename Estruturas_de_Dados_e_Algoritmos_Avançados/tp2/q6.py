class GrafoListaAdjacencia:
    def __init__(self):
        self.grafo = {}

    def adiciona_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adiciona_aresta(self, v1, v2):
        if v1 in self.grafo and v2 in self.grafo:
            self.grafo[v1].append(v2)
            self.grafo[v2].append(v1)

    def imprime_pares_relacionados(self):
        arestas_impressas = set()
        for vertice, vizinhos in self.grafo.items():
            for vizinho in vizinhos:
                if (vizinho, vertice) not in arestas_impressas and (vertice, vizinho) not in arestas_impressas:
                    print(f"({vertice}, {vizinho})")
                    arestas_impressas.add((vertice, vizinho))

grafo = GrafoListaAdjacencia()

vertices = ["broca", "martelo", "serra", "faca", "colher", "garfo", "pregos", 
            "alfinetes", "agulhas", "esmalte", "sombra", "escova", "oculos"]
for vertice in vertices:
    grafo.adiciona_vertice(vertice)

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

for vertice, vizinhos in arestas.items():
    for vizinho in vizinhos:
        grafo.adiciona_aresta(vertice, vizinho)

grafo.imprime_pares_relacionados()
