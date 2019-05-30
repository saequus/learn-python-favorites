def binary_search(arr, l, r, target):
    if r >= l: 
        mid = l + (r-l) // 2

        if arr[mid] == target:
            return mid 
          
        if arr[mid] > target:
            return binary_search(arr, l, mid - 1, target)
        return binary_search(arr, mid + 1, r, target)
    return -1


def exponential_search(arr, n, target):
    if arr[0] == target:
        return 0
          
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2

    return binary_search(arr, i//2, min(i, n), target)
      
  
numbers = [2, 3, 4, 5, 7, 10, 12, 23, 33, 36, 38, 40]
length = len(numbers)
x = 23
print(exponential_search(numbers, length, x))


