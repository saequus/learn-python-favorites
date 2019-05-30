# Сортировка слиянием. Вычислительная сложность: n log n (для всех случаев)
# Сложность по памяти O(n). Свойства: устойчивая.
# Алгоритм сортировки называется устойчивым (stable), если он сохраняет
# относительный порядок следования одинаковых ключей.


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_part = arr[:mid]  # Dividing the array elements
        right_part = arr[mid:]  # into 2 halves

        merge_sort(left_part)
        merge_sort(right_part)

        i = j = k = 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1


a = [3, 6, 12, 33, 54, 32, 5, 8, 9, 10, 48, 44]
print(merge_sort(a))
print(a)





