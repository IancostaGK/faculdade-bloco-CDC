class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.seq_count = 0

    def push(self, nome, gravidade):
        entry = (-gravidade, self.seq_count, nome)
        self.seq_count += 1
        self.heap.append(entry)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 0:
            top_priority = self.heap[0]
            last_entry = self.heap.pop()
            if len(self.heap) > 0:
                self.heap[0] = last_entry
                self._sift_down(0)
            return top_priority[-1]
        else:
            raise IndexError("pop from an empty priority queue")

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0][-1]
        else:
            raise IndexError("peek from an empty priority queue")

    def _sift_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def _sift_down(self, index):
        max_index = len(self.heap) - 1
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            min_index = index

            if left_child_index <= max_index and self.heap[left_child_index] < self.heap[min_index]:
                min_index = left_child_index
            if right_child_index <= max_index and self.heap[right_child_index] < self.heap[min_index]:
                min_index = right_child_index

            if min_index != index:
                self.heap[min_index], self.heap[index] = self.heap[index], self.heap[min_index]
                index = min_index
            else:
                break

# Exemplo de uso
fila_emergencia = PriorityQueue()
fila_emergencia.push("José", 2)
fila_emergencia.push("Márcia", 3)
fila_emergencia.push("André", 2)
fila_emergencia.push("Bruna", 5)

while len(fila_emergencia.heap) > 0:
    paciente = fila_emergencia.pop()
    print(f"Atendendo paciente: {paciente}")
