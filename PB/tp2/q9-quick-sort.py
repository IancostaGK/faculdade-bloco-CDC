def quick_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

with open('pb/tp2/arquivos.txt', 'r') as file:
    content = file.read().splitlines()

quick_sort(content)
print("Arquivos ordenados com Quick Sort:")
print(content)
