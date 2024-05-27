import math
import numpy as np
from numba import jit, prange

graph = np.array(
    [[0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]])

@jit(nopython=True)
def dijkstra(graph, src):
    V = graph.shape[0]
    dist = np.full(V, math.inf)
    dist[src] = 0
    visited = np.zeros(V, dtype=np.int32)
    
    for _ in prange(V):
        u = -1
        min_dist = math.inf
        for v in prange(V):
            if not visited[v] and dist[v] < min_dist:
                u = v
                min_dist = dist[v]
        
        visited[u] = 1
        
        for v in prange(V):
            if not visited[v] and graph[u, v] != 0 and dist[u] + graph[u, v] < dist[v]:
                dist[v] = dist[u] + graph[u, v]
    
    return dist

src_vertex = 0
result = dijkstra(graph, src_vertex)

print("Distâncias mínimas do vértice {}:".format(src_vertex))
for i, dist in enumerate(result):
    print("Para o vértice {}: {}".format(i, dist))
