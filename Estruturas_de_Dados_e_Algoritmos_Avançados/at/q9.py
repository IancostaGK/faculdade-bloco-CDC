def numero_faltante(array):
  n = len(array)
  soma_esperada = n * (n + 1) // 2
  soma_atual = sum(array)
  return soma_esperada - soma_atual

print(numero_faltante([2, 3, 0, 6, 1, 5])) 
print(numero_faltante([8, 2, 3, 9, 4, 7, 5, 0, 6]))  
