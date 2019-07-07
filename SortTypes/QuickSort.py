# Алгоритм быстрой сортировки
# В среднем случае он работает за время Θ(𝑛log𝑛) и требует порядка Θ(log𝑛)
# ячеек памяти на поддержание рекурсивных вызовов. Однако алгоритм не
# обладает свойством устойчивости и в худшем случае требует выполнения
# порядка Θ(𝑛2) операций.

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot.


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index


def quick_sort_helper(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)


a = [3, 1, 14, 23, 55, 31, 15, 7, 8, 18]
b = [2, 5, 3, 1, 23, 15, 16, 13, 22, 19, 44, 32, 38, 7]
t = [2, 19, 22, 12, 3, 1, 7, 55, 32, 21, 2, 45, 32, 9]
quick_sort(a)
quick_sort(b)
quick_sort(t)
print(a)
print(b)
print(t)


