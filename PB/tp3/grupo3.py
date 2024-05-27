import time
import random
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

#10. Implemente o procedimento padrão que faça um atravessamento em nível de uma árvore binária.
def level_order_traversal(root):
    result = []
    if root is None:
        return result
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


#11. Proponha e implemente uma versão paralela do algoritmo implementado na questão 10.
def level_order_traversal_parallel(root):
    if root is None:
        return []

    result = []
    queue = [root]

    def worker(node):
        nonlocal result
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    with ThreadPoolExecutor() as executor:
        while queue:
            node = queue.pop(0)
            executor.submit(worker, node)

    return result


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def create_random_tree(size):
    root = None
    for _ in range(size):
        root = insert(root, random.randint(1, 100))
    return root

#9. Escreva um algoritmo de busca paralelo que encontre o maior valor armazenado em uma árvore binária de busca.
def find_max(root):
    if root is None:
        return float('-inf')
    return max(root.value, find_max(root.left), find_max(root.right))


#12. Compare os resultados obtidos com as versões implementadas nas questões 10 e 11, em termos do desempenho computacional. Plote os resultados em um gráfico.
def compare_performance():
    sizes = [100, 1000, 5000, 10000]
    sequential_times = []
    parallel_times = []

    for size in sizes:
        tree = create_random_tree(size)

        start = time.time()
        level_order_traversal(tree)
        end = time.time()
        sequential_times.append(end - start)

        start = time.time()
        level_order_traversal_parallel(tree)
        end = time.time()
        parallel_times.append(end - start)

    plt.plot(sizes, sequential_times, label='Sequential')
    plt.plot(sizes, parallel_times, label='Parallel')
    plt.xlabel('Tree Size')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Sequential vs Parallel Level Order Traversal')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # Exemplo de uso
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Level Order Traversal:", level_order_traversal(root))

    tree = create_random_tree(1000)
    max_value_sequential = find_max(tree)
    print(f'Max value (Sequential): {max_value_sequential}')

    compare_performance()
