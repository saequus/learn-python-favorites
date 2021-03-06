# ============================================================================
# ========================== CountSort Algorithm =============================
# ============================================================================


def count_sort(arr):
    output = [0 for _ in range(256)]

    # Create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for _ in range(256)]

    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[ord(i)] += 1
    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i - 1]

    # Build the output character array
    for i in arr:
        output[count[ord(i)] - 1] = i
        count[ord(i)] -= 1
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


a = 'work having no sleep and try to sort it'
ans = count_sort(a)
print(ans)

