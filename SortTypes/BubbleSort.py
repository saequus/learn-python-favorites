# Сортировка пузырьком.
# Вычислительная сложность:
# В худшем случае – O(n^2).
# В лучшем случае (если уже отсортирован) – O(n).
# Сложность по памяти: O(n). Дополнительная память: O(1).
# Свойства: относится к классу алгоритмов сортировки
# на месте (in-place sort), устойчив.
# Алгоритм сортировки называется устойчивым (stable), если он сохраняет
# относительный порядок следования одинаковых ключей.


def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        not_swapped = True
        # traverse the array from 0 to
        # n-i-1. Swap if the element
        # found is greater than the
        # next element
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                not_swapped = False
        # IF no two elements were swapped
        # by inner loop, then break
        if not_swapped:
            break


b = [3, 5, 1, 30, 32, 6, 34, 14, 16, 66, 48]
optimized_bubble_sort(b)
print(b)


