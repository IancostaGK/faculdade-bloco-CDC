import grafos as grf

amigos = grf.Grafo()

a = amigos.cria_vertice("A")
b = amigos.cria_vertice("B")
c = amigos.cria_vertice("C")
d = amigos.cria_vertice("D")
e = amigos.cria_vertice("E")
f = amigos.cria_vertice("F")
g = amigos.cria_vertice("G")
h = amigos.cria_vertice("H")
i = amigos.cria_vertice("I")
j = amigos.cria_vertice("J")
k = amigos.cria_vertice("K")
l = amigos.cria_vertice("L")
m = amigos.cria_vertice("M")
n = amigos.cria_vertice("N")
o = amigos.cria_vertice("O")
p = amigos.cria_vertice("P")

amigos.adiciona_aresta(a, b)
amigos.adiciona_aresta(a, d)
amigos.adiciona_aresta(a, c)
amigos.adiciona_aresta(b, e)
amigos.adiciona_aresta(b, f)
amigos.adiciona_aresta(e, j)
amigos.adiciona_aresta(f, j)
amigos.adiciona_aresta(j, o)
amigos.adiciona_aresta(c, g)
amigos.adiciona_aresta(g, k)
amigos.adiciona_aresta(d, i)
amigos.adiciona_aresta(d, h)
amigos.adiciona_aresta(h, l)
amigos.adiciona_aresta(h, m)
amigos.adiciona_aresta(m, i)
amigos.adiciona_aresta(i, n)
amigos.adiciona_aresta(n, p)


caminho = grf.busca_dfs_caminho(o, p)
if caminho:
      print("Caminho de O a P:", caminho)
else:
      print("Não há caminho de O a P.")

amigos.desenha()