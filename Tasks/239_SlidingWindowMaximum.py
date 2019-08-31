from collections import deque


def max_sliding_window(arr, k):
    if not arr or k == 0:
        return []
    maxes = []
    q = deque()
    for i, j in enumerate(arr):
        while q and q[-1] < i - k + 1:
            q.pop()
        while q and arr[q[0]] < arr[i]:
            q.popleft()
        q.appendleft(i)
        if i >= k - 1:
            maxes.append(arr[q[-1]])
    return maxes


def min_sliding_window(arr, k):
    q = deque()
    minimums = []
    for i, j in enumerate(arr):
        while q and i > q[-1] + k - 1:
            q.pop()
        while q and j < arr[q[0]]:
            q.popleft()
        q.appendleft(i)
        if i >= k - 1:
            minimums.append(arr[q[-1]])
    return minimums


# Driver code

nums = [1, 3, -1, -3, 5, 3, 6, 7, 10, 12, 34, 22, -2, -3, -12, 3, 4, 54]
window_length = 5

result = max_sliding_window(nums, window_length)
print('max_sliding_window')
print('result:', result)
print('expected: [5, 5, 6, 7, 10, 12, 34, 34, 34, 34, 34, 22, 4, 54]')

result = min_sliding_window(nums, window_length)
print('min_sliding_window')
print('result', result)
print('expected: [-3, -3, -3, -3, 3, 3, 6, 7, -2, -3, -12, -12, -12, -12]')
