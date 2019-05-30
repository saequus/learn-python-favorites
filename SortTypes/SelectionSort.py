# Сортировка выбором (selection sort).
# Вычислительная сложность: Θ(𝑛^2)
# Сложность по памяти: 𝑂(1). Свойства: устойчивость зависит от реализации.
# Stability: The default implementation is not stable. However it can be made stable.
# Алгоритм сортировки называется устойчивым (stable), если он сохраняет
# относительный порядок следования одинаковых ключей.


def selection_sort(arr):
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


a = [3, 5, 1, 30, 32, 6, 34, 14, 16, 66, 48]
selection_sort(a)
print(a)


