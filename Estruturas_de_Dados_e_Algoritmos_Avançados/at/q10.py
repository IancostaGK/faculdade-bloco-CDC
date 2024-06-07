def maior_produto(array):
  if len(array) < 2:
    return None 

  maior1 = maior2 = float('-inf')
  menor1 = menor2 = float('inf')

  for num in array:
    if num > maior1:
      maior2 = maior1
      maior1 = num
    elif num > maior2:
      maior2 = num
    
    if num < menor1:
      menor2 = menor1
      menor1 = num
    elif num < menor2:
      menor2 = num

  return max(maior1 * maior2, menor1 * menor2)

# Exemplos de uso
print(maior_produto([5, -10, -6, 9, 4]))  
