class Heap:
    def __init__(self):
        self.heap_list = []

    def insert(self, item):
        self.heap_list.append(item)
        self._heapify_up(len(self.heap_list) - 1)

    def remove(self):
        if len(self.heap_list) == 0:
            raise IndexError("Heap is empty")
        last_element = self.heap_list.pop()
        if len(self.heap_list) > 0:
            removed_item = self.heap_list[0]
            self.heap_list[0] = last_element
            self._heapify_down(0)
            return removed_item
        return last_element

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap_list[index] > self.heap_list[parent_index]:
            self.heap_list[index], self.heap_list[parent_index] = (
                self.heap_list[parent_index],
                self.heap_list[index],
            )
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index
        if (
            left_child_index < len(self.heap_list)
            and self.heap_list[left_child_index] > self.heap_list[largest]
        ):
            largest = left_child_index
        if (
            right_child_index < len(self.heap_list)
            and self.heap_list[right_child_index] > self.heap_list[largest]
        ):
            largest = right_child_index
        if largest != index:
            self.heap_list[index], self.heap_list[largest] = (
                self.heap_list[largest],
                self.heap_list[index],
            )
            self._heapify_down(largest)

    def niveis(self):
        n = len(self.heap_list)
        return n.bit_length() if n > 0 else 0

heap = Heap()
heap.insert(10)
heap.insert(5)
heap.insert(15)
heap.insert(3)
heap.insert(8)
print("Número de níveis:", heap.niveis()) 
