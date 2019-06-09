def binary_search(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        return -1


a = [2, 3, 4, 10, 22, 24, 30, 35, 40]
x = 30

result = binary_search(a, 0, len(a) - 1, x)
print(result)
