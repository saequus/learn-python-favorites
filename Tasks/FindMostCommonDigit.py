# ============================================================================
# ============================== Find The Biggest  ===========================
# ============================ and Most Common Digit =========================
# ============================================================================


import collections

n = int(input())
array = input().split(' ')


def find_most_common_digit(array):
    s = set(digit for digit in array)
    count = collections.Counter(
        digit for digit in array)

    result, best = [], 0
    for digit in s:
        if count[digit] > best:
            best = count[digit]
            result = []
        if count[digit] == best:
            result.append(int(digit))

    return max(result)


print_result = find_most_common_digit(array)
print(print_result)

# Examples:
#
# Example 1
# 3
# 3 3 3
# Result 1
# 3
#
# Example 2
# 5
# 4 1 4 3 3
# Result 2
# 4
#
# Example 3
# 10
# 10 6 10 10 10 10 8 8 10 9
# Result 3
# 10
