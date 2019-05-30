# Пирамидаль- ная сортировка (heap sort). Вычислительная мощность: Θ(𝑛 log 𝑛).
# Сложность по памяти: 𝑂(1). Свойства: неустойчивая.
# Алгоритм сортировки называется устойчивым (stable), если он сохраняет
# относительный порядок следования одинаковых ключей.

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    if l < n and arr[i] < arr[l]:  # See if left child of root exists and is greater than root
        largest = l
    if r < n and arr[largest] < arr[r]:  # See if right child of root exists and is greater than largest
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
