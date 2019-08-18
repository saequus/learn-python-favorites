# ============================================================================
# ========================= RadixSort Algorithm ==============================
# ============================================================================

def radix_sort(arr):
    radix = 10
    max_length = False
    placement = 1

    while not max_length:
        max_length = True
        buckets = [[] for _ in range(radix)]

        for i in arr:
            tmp = i / placement
            buckets[int(tmp % radix)].append(i)
            if max_length and tmp > 0:
                max_length = False

        k = 0
        for b in range(radix):
            for i in buckets[b]:
                arr[k] = i
                k += 1

        placement *= radix


a = [17, 10, 45, 75, 90, 80, 2, 24, 6, 1, 85, 36]
b = [3, 6, 1, 2, 21, 33, 25, 34, 39, 20, 12, 15, 17, 9]
radix_sort(a)
print(a)
radix_sort(b)
print(b)

