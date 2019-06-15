# Reverse Number (Print Number Backwards)
# Given integers 1204900, 431, -453. The func must return 94021, 134, -354


def reverse_number(num) -> str:  # not the fastest, optimise
    """ Reverse number.
    Keep negative if needed. Remove zeros if ended with 0.
    :param: num
    :return: str
    """
    res = list()
    neg = 0
    num = int(num)
    if num < 0:
        num *= -1
        neg = 1
    while num % 10 == 0:
        num /= 10
    num = list(str(int(num)))
    for i in range(len(num)):
        res.append(num[-i - 1])
    res = ''.join(str(res[j]) for j in range(len(num)))
    res = int(res)
    if neg == 1:
        res *= -1

    return 'Reversed number is %d' % res


# Driver Code

first = 1204900
second = 431
third = -453
print(reverse_number(first))
print(reverse_number(second))
print(reverse_number(third))

