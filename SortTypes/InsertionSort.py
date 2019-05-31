# Сортировка слиянием. Вычислительная сложность:
# Θ(n^2 ) для худшего случая,
# Θ(𝑛^2 ) для среднего случая,
# Θ(𝑛) для лучшего случая.
# Сложность по памяти O(1). Свойства: устойчивая, online.
# Алгоритм сортировки вставкой является устойчивым, так как не меняет
# относительный порядок следования одинаковых ключей. В процессе
# своей работ алгоритм использует константное число дополнительных ячеек
# памяти (переменные 𝑖, 𝑘𝑒𝑦 и 𝑗), что относит его к классу алгоритмов сортировки
# на месте (in-place sort). Кроме того, алгоритм относится к классу
# online-алгоритмов – обеспечивает возможность упорядочивания массивов при
# динамическом поступлении новых элементов.
# Алгоритм сортировки называется устойчивым (stable), если он сохраняет
# относительный порядок следования одинаковых ключей.


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:  # in order to make sort reverse change to key > arr[j]
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


a = [3, 5, 1, 30, 32, 6, 34, 14, 16, 66, 48]
insertion_sort(a)
print(a)
