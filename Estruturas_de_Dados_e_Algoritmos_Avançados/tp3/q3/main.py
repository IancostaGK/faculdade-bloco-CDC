import grafos as grf

amigos = grf.Grafo()

alice = amigos.cria_vertice("Alice")
bob = amigos.cria_vertice("Bob")
cynthia = amigos.cria_vertice("Cynthia")
diana = amigos.cria_vertice("Diana")
elise = amigos.cria_vertice("Elise")
fred = amigos.cria_vertice("Fred")
jamal = amigos.cria_vertice("Jamal")
melvyn = amigos.cria_vertice("Melvyn")
rodrigo = amigos.cria_vertice("Rodrigo")
stella = amigos.cria_vertice("Stella")
vicky = amigos.cria_vertice("Vicky")

amigos.adiciona_aresta(alice, bob)
amigos.adiciona_aresta(bob, cynthia)
amigos.adiciona_aresta(alice, diana)
amigos.adiciona_aresta(bob, diana)
amigos.adiciona_aresta(elise, fred)
amigos.adiciona_aresta(diana, fred)
amigos.adiciona_aresta(fred, alice)
amigos.adiciona_aresta(rodrigo, melvyn)
amigos.adiciona_aresta(stella, jamal)

componente_conexa = grf.travessia_bfs(alice)
componente_conexa.remove(alice)
print("Conectados a Alice:", 
      grf.travessia_bfs(alice) - {alice})
print("Conectados a Rodrigo:", 
      grf.travessia_bfs(rodrigo) - {rodrigo})
print("Conectados a Jamal:", 
      grf.travessia_bfs(jamal) - {jamal})

print("Existe caminho entre Alice e Bob:", amigos.busca_caminho_bfs(alice, bob))
print("Existe caminho entre Alice e Cynthia:", amigos.busca_caminho_bfs(alice, cynthia))
print("Existe caminho entre Alice e Melvyn:", amigos.busca_caminho_bfs(alice, melvyn))

amigos.desenha()
