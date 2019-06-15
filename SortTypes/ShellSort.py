# Time complexity of above implementation of shellsort is O(n2). In this
# implementation gap is reduce by half in every iteration. There are many
# other ways to reduce gap which lead to better time complexity.


def gap_ins_sort(arr, low, gap):
    for i in range(low + gap, len(arr), gap):
        current = arr[i]
        position = i
        while position >= gap and arr[position - gap] > current:
            arr[position] = arr[position - gap]
            position = position - gap
        arr[position] = current


def shell_sort(array):
    increment = len(array) // 2
    while increment > 0:
        for startPosition in range(increment):
            gap_ins_sort(array, startPosition, increment)
        increment //= 2


p = [3, 12, 32, 21, 44, 35, 7, 9, 11, 10]
shell_sort(p)
print(p)


