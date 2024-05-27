def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Array ordenado:", arr)
