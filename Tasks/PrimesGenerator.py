def gen_primes() -> int:
    """ Generate an infinite sequence of prime numbers.
    :return: int
    """
    table = {}
    i = 2
    while True:
        if i not in table:
            yield i
            table[i * i] = [i]
        else:
            for previous in table[i]:
                table.setdefault(previous + i, []).append(previous)
            del table[i]

        i += 1


i = 0
x = gen_primes()
while i < 20:
    print(next(x))
    i += 1
