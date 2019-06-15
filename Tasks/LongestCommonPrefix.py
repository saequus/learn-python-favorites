# LeetCode 14. Longest Common Prefix

x = ['What if I could swim', 'What is it?', 'Where are sweets']
y = ["flower", "flow", "flight"]


def longest_common_prefix(words) -> str:
    """ Return longest common prefix for all words in the list.
    :param: list (words)
    :return: str
    """
    if not words or len(words) == 0:
        return ""
    prefix = words[0]

    for i in range(1, len(words)):
        j = 0
        while j < min(len(prefix), len(words[i])):
            if prefix[j] != words[i][j]:
                break
            j += 1
        prefix = prefix[:j]
    return prefix


print(longest_common_prefix(x))
print(longest_common_prefix(y))
