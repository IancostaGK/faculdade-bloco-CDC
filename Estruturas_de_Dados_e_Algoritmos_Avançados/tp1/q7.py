class PriorityQueueSortedArray:
    def __init__(self):
        self.queue = []

    def push(self, nome, gravidade):
        entry = {"nome": nome, "gravidade": gravidade}
        index = self._find_insertion_index(gravidade)
        self.queue.insert(index, entry)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)["nome"]
        else:
            raise IndexError("pop from an empty priority queue")

    def peek(self):
        if self.queue:
            return self.queue[0]["nome"]
        else:
            raise IndexError("peek from an empty priority queue")

    def _find_insertion_index(self, gravidade):
        for i, entry in enumerate(self.queue):
            if gravidade < entry["gravidade"]:
                return i
        return len(self.queue)

fila_emergencia = PriorityQueueSortedArray()
fila_emergencia.push("José", 2)
fila_emergencia.push("Márcia", 3)
fila_emergencia.push("André", 2)
fila_emergencia.push("Bruna", 5)

while fila_emergencia.queue:
    paciente = fila_emergencia.pop()
    print(f"Atendendo paciente: {paciente}")
