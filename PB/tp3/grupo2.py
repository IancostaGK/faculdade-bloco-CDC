import time
from multiprocessing import Pool
import time
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
import numpy as np

#q5 .
def parallel_sort(arr, num_processes=2):
    def sort_part(arr_part):
        return sorted(arr_part)
    arr_parts = np.array_split(arr, num_processes)
    sorted_parts = Parallel(n_jobs=num_processes)(delayed(sort_part)(part) for part in arr_parts)
    sorted_arr = sorted(sum(sorted_parts, []))

    return sorted_arr


# q6 and #q7
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.writelines(content)

# q6
def k_way_merge(arrays):
    merged_array = []

    while any(arrays):
        min_vals = [min(a) if a else float('inf') for a in arrays]
        min_idx = min_vals.index(min(min_vals))
        merged_array.append(min_vals[min_idx])
        arrays[min_idx].remove(min_vals[min_idx])

    return merged_array

# q7
def k_way_merge_parallel(arrays):
    arrays = [s.lower() for sublist in arrays for s in sublist]

    with Pool() as pool:
        sorted_content = pool.map(str, arrays)
        sorted_content.sort()

    return sorted_content  

if __name__ == "__main__":
    #5. Implemente um algoritmo de ordenação paralela (de sua escolha) usando OpenMP
    arr = np.random.randint(0, 100, size=10)
    print("Array original:", arr)

    sorted_arr = parallel_sort(arr)
    print("Array ordenado:", sorted_arr)

    #6 e 7. Faça uma pesquisa sobre o algoritmo de ordenação externa chamado k-way merge e implemente sua versão padrão
    file_path = 'pb/tp3/arquivos.txt'
    content = read_file(file_path)

    content = [line.strip() for line in content if line.strip()]

    sorted_content = k_way_merge([content])
    sorted_content_parallel = k_way_merge_parallel([content])

    print("Conteúdo do arquivo ordenado:")
    print('\n'.join(sorted_content))

    print("Conteúdo do arquivo ordenado (versão paralela):")
    print('\n'.join(sorted_content_parallel))

    #8.Compare os resultados obtidos com as versões implementadas nas questões 6 e 7, em termos do desempenho computacional. Plote os resultados em um gráfico.

    times_parallel = []
    times_sequential = []

    start_time = time.time()
    result_parallel = k_way_merge_parallel([content])
    end_time = time.time()
    times_parallel.append(end_time - start_time)
    print(end_time - start_time)

    start_time = time.time()
    result_sequential = k_way_merge([content])
    end_time = time.time()
    times_sequential.append(end_time - start_time)
    print(end_time - start_time)

    # Plotar os resultados
    labels = ['Versão Paralela', 'Versão Sequencial']
    times = [times_parallel[0], times_sequential[0]]

    plt.bar(labels, times)
    plt.xlabel('Versão do Algoritmo')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Comparação de Desempenho')
    plt.show()

