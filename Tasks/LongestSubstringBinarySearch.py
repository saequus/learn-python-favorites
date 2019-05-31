newline = ['ghost,e', 'ghost23nd', 'ghostcmcn ']
def longestPrefix(words):
    minL = 100
    minL = min(len(word) for word in words if len(word) < minL)
    high = minL
    low = 0
    while low <= high:
        middle = (low + high) // 2
        if isCommonPrefix2(words, middle):
            low = middle + 1
        else:
            high = middle - 1
    return words[0][:(high + low) // 2]


def isCommonPrefix2(words, mid):
    s = words[0][:mid]
    for i in range(len(words)):
        if not words[i].startswith(s):
            return False
    return True


print(longestPrefix(newline))