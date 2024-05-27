class Heap:
    def __init__(self, type='max'):
        self.heap = []
        self.type = type

    def insert(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        if index <= 0:
            return
        parent = (index - 1) // 2
        if (self.type == 'max' and self.heap[index] > self.heap[parent]) \
                or (self.type == 'min' and self.heap[index] < self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)

    def delete(self, item):
        if item not in self.heap:
            raise ValueError("Item not found in the heap")
        index = self.heap.index(item)
        last = len(self.heap) - 1
        self.heap[index], self.heap[last] = self.heap[last], self.heap[index]
        self.heap.pop()
        self._bubble_down(index)

    def _bubble_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index if self.type == 'max' else None
        smallest = index if self.type == 'min' else None

        if left_child < len(self.heap):
            if self.type == 'max' and self.heap[left_child] > self.heap[largest]:
                largest = left_child
            elif self.type == 'min' and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child

        if right_child < len(self.heap):
            if self.type == 'max' and self.heap[right_child] > self.heap[largest]:
                largest = right_child
            elif self.type == 'min' and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

        if largest != index and self.type == 'max':
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._bubble_down(largest)
        elif smallest != index and self.type == 'min':
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    def search(self, item):
        return item in self.heap


# 1. Escreva um programa para criar uma heap máxima. Para isso, implemente uma função/método para inserção de elementos que respeite e preserve as propriedades de uma heap máxima.
max_heap = Heap()
max_heap.insert(10)
max_heap.insert(30)
max_heap.insert(20)
max_heap.insert(40)
print("Heap Máxima:", max_heap.heap)

# 2. Inclua uma função/método para executar a deleção de elementos da heap no seu programa da questão 1.
max_heap.delete(30)
print("Heap Máxima após deleção:", max_heap.heap)

#3. Inclua uma função/método para executar buscas por elementos da heap no seu programa da questão 1.
print("Busca por 20 na Heap Máxima:", max_heap.search(20))

#4. Crie uma versão de seu programa da questão 1 para gerar uma heap mínima.
min_heap = Heap(type='min')
min_heap.insert(10)
min_heap.insert(30)
min_heap.insert(20)
min_heap.insert(40)
print("Heap Mínima:", min_heap.heap)

#5. Faça as adaptações necessárias nos códigos das questões 2 e 3 para que passem a operar sobre uma heap mínima e inclua-os no seu programa da questão 4.

# Deletando um elemento da heap mínima
min_heap.delete(20)
print("Heap Mínima após deleção:", min_heap.heap)

# Buscando elementos na heap mínima
print("Busca por 30 na Heap Mínima:", min_heap.search(30))
