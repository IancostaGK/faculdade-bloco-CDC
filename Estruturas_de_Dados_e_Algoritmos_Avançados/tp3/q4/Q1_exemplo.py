import grafos as grf

letras = grf.Grafo()

a = letras.cria_vertice("A")
b = letras.cria_vertice("B")
c = letras.cria_vertice("C")
d = letras.cria_vertice("D")
e = letras.cria_vertice("E")
f = letras.cria_vertice("F")
g = letras.cria_vertice("G")
h = letras.cria_vertice("H")
i = letras.cria_vertice("I")
j = letras.cria_vertice("J")
k = letras.cria_vertice("K")
l = letras.cria_vertice("L")
m = letras.cria_vertice("M")
n = letras.cria_vertice("N")
o = letras.cria_vertice("O")
p = letras.cria_vertice("P")

letras.adiciona_aresta(a, b)
letras.adiciona_aresta(a, d)
letras.adiciona_aresta(a, c)
letras.adiciona_aresta(b, e)
letras.adiciona_aresta(b, f)
letras.adiciona_aresta(e, j)
letras.adiciona_aresta(f, j)
letras.adiciona_aresta(j, o)
letras.adiciona_aresta(c, g)
letras.adiciona_aresta(g, k)
letras.adiciona_aresta(d, i)
letras.adiciona_aresta(d, h)
letras.adiciona_aresta(h, l)
letras.adiciona_aresta(h, m)
letras.adiciona_aresta(m, i)
letras.adiciona_aresta(i, n)
letras.adiciona_aresta(n, p)


caminho = grf.busca_dfs_caminho(o, p)
if caminho:
      print("Caminho de O a P:", caminho)
else:
      print("Não há caminho de O a P.")

letras.desenha()