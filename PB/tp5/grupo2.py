def valor_peso(item):
  return item[2] / item[1]

def valor(item):
  return item[2]

def peso(item):
  return item[1]

def mochila_binaria(capacidade, itens):
  # Ordena os itens pela razão valor/peso em ordem decrescente
  itens.sort(key=lambda item: item[2] / item[1], reverse=True)
  
  valor_total = 0
  peso_total = 0
  mochila = []
  
  for item in itens:
    if peso_total + item[1] <= capacidade:
      mochila.append(item)
      peso_total += item[1]
      valor_total += item[2]
  
  return mochila, valor_total, peso_total

def mochila_inteira(capacidade, itens):
  # Ordena os itens pela razão valor/peso em ordem decrescente
  itens.sort(key=lambda item: item[2] / item[1], reverse=True)
  
  valor_total = 0
  peso_total = 0
  mochila = []
  
  for item in itens:
    while peso_total + item[1] <= capacidade:
      mochila.append(item)
      peso_total += item[1]
      valor_total += item[2]
  
  return mochila, valor_total, peso_total

def mochila_compartimentada(capacidades, itens):
  # Ordena os itens pela razão valor/peso em ordem decrescente
  itens.sort(key=lambda item: item[2] / item[1], reverse=True)
  
  valor_total = 0
  mochilas = [[] for _ in capacidades]
  pesos_mochilas = [0] * len(capacidades)
  
  for item in itens:
    for i in range(len(capacidades)):
      if pesos_mochilas[i] + item[1] <= capacidades[i]:
        mochilas[i].append(item)
        pesos_mochilas[i] += item[1]
        valor_total += item[2]
        break
  
  return mochilas, valor_total, pesos_mochilas

# Exemplo de uso das funções

capacidade_binaria = 400
capacidade_inteira = 400
capacidades_compartimentada = [200, 150, 100]

itens = [
  ("mapa", 9, 150),
  ("bússola", 13, 35),
  ("água", 178, 200),
  ("sanduíche", 50, 160),
  ("açúcar", 15, 60),
  ("lata", 68, 45),
  ("banana", 27, 60),
  ("maçã", 39, 40),
  ("queijo", 23, 30),
  ("cerveja", 52, 10),
  ("creme bronzeador", 11, 70),
  ("câmera", 32, 30),
  ("camiseta", 24, 15),
  ("calças", 48, 10),
  ("guarda-chuva", 73, 40),
  ("calças impermeáveis", 42, 70),
  ("capa de chuva", 43, 75),
  ("carteira", 22, 80),
  ("óculos de sol", 7, 20),
  ("toalha", 18, 12),
  ("meias", 4, 50),
  ("livro", 30, 10)
]

# Mochila Binária
mochila, valor_total, peso_total = mochila_binaria(capacidade_binaria, itens)
print("Mochila Binária:")
print(f"Itens na mochila: {mochila}")
print(f"Valor total: {valor_total}")
print(f"Peso total: {peso_total}\n")

# Mochila Inteira
mochila, valor_total, peso_total = mochila_inteira(capacidade_inteira, itens)
print("Mochila Inteira:")
print(f"Itens na mochila: {mochila}")
print(f"Valor total: {valor_total}")
print(f"Peso total: {peso_total}\n")

# Mochila Compartimentada
mochilas, valor_total, pesos_mochilas = mochila_compartimentada(capacidades_compartimentada, itens)
print("Mochila Compartimentada:")
for i, mochila in enumerate(mochilas):
  print(f"Mochila {i+1}: {mochila}, Peso total: {pesos_mochilas[i]}")
print(f"Valor total: {valor_total}")
