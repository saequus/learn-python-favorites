# Bag of Tokens. Task 948)
# https://leetcode.com/problems/bag-of-tokens/


def tokens_number(tokens, total_price):
    """
    :type tokens: List[int]
    :type total_price: int
    :rtype: int
    """
    total = 0
    i = 0
    tokens = sorted(tokens)
    while tokens and total_price // tokens[i] >= 1:
        total += 1
        total_price -= tokens[i] * 1
        tokens.pop(i)
    return total


n = [100, 200, 400, 600, 700, 400, 50, 1200]


print(tokens_number(n, 1000))
print(tokens_number(n, 450))
print(tokens_number(n, 200))
