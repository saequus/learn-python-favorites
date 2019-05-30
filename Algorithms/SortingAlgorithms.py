# Сортировки выбором
# O(n)2 – selection: pancake (пузырькова сортировка), cycle, double selection (шейкерная), bingo (бинго-сортировка)
# O(n log n) – heaps: heap weak, ternary heap, tournament, binomical heap, j, introspective
# O(n) – cartesian, smooth

n = [3, 5, 12, 2, 10, 6, 4, 1, 9, 10, 1, 2, 4, 12, 9]


def pancake_sort(data):
    for i, e in enumerate(data):
        mn = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[mn] = data[mn], e
    return data


def bingo(data):
    # Первый проход.

    mx = len(data) - 1
    nextValue = data[mx]
    for i in range(mx - 1, -1, -1):
        if data[i] > nextValue:
            nextValue = data[i]

    while mx and data[mx] == nextValue:
        mx -= 1

    # Последующие проходы.

    while mx:
        value = nextValue
        nextValue = data[mx]
        for i in range(mx - 1, -1, -1):
            if data[i] == value:
                data[i], data[mx] = data[mx], data[i]
                mx -= 1
            elif data[i] > nextValue:
                nextValue = data[i]
        while mx and data[mx] == nextValue:
            mx -= 1

    return data



