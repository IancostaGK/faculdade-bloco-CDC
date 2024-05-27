import ipaddress
import time
import matplotlib.pyplot as plt

class PrefixTree:
    def __init__(self):
        self.root = {}

    def insert(self, prefix):
        node = self.root
        for bit in prefix:
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def search(self, prefix):
        node = self.root
        for bit in prefix:
            if bit not in node:
                return False
            node = node[bit]
        return True

def generate_ipv6_prefixes(size):
    prefixes = []
    for i in range(size):
        prefix = ipaddress.IPv6Network('2001:db8::/32').compressed
        prefixes.append(prefix)
    return prefixes

def test_performance(prefix_tree, ipv6_prefixes):
    times = []
    for prefix in ipv6_prefixes:
        start_time = time.time()
        prefix_tree.search(prefix)
        end_time = time.time()
        execution_time = end_time - start_time
        times.append(execution_time)
    return times

def plot_performance(prefix_sizes, execution_times):
    plt.plot(prefix_sizes, execution_times)
    plt.xlabel('Número de Prefixos IPv6')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Desempenho da Busca de Prefixos IPv6')
    plt.show()

if __name__ == '__main__':
    #13. Implemente um algoritmo de busca binária para prefixos IPv4 (use uma árvore binária como estrutura de dados para suporte)
    ipv4_tree = PrefixTree()
    ipv4_prefixes = ['192.168.1.0/24', '10.0.0.0/8', '172.16.0.0/12']
    for prefix in ipv4_prefixes:
        ipv4_tree.insert(ipaddress.IPv4Network(prefix).compressed)

    #14. Adaptar o seu algoritmo de busca binária implementado na questão 13 para suportar também prefixos IPv6.
    ipv6_tree = PrefixTree()
    ipv6_prefixes = generate_ipv6_prefixes(1000)  # Exemplo com 1000 prefixos IPv6
    for prefix in ipv6_prefixes:
        ipv6_tree.insert(ipaddress.IPv6Network(prefix).compressed)

    #15. Realize testes do desempenho de seu algoritmo de busca implementado na questão 14 com diferentes tamanhos de prefixos IPv6. Exiba os resultados em um gráfico
    prefix_sizes = [10, 100, 1000, 10000] 
    execution_times = []
    for size in prefix_sizes:
        ipv6_prefixes = generate_ipv6_prefixes(size)
        ipv6_tree = PrefixTree()
        for prefix in ipv6_prefixes:
            ipv6_tree.insert(ipaddress.IPv6Network(prefix).compressed)
        times = test_performance(ipv6_tree, ipv6_prefixes)
        execution_times.append(sum(times) / len(times))  

    plot_performance(prefix_sizes, execution_times)
