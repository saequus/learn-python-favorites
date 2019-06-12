def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    current = {}
    element = 2
    while True:
        if element not in current:
            yield element
            current[element * element] = [element]
        else:
            for p in current[element]:
                current.setdefault(p + element, []).append(p)
            del current[element]

        element += 1


i = 0
x = gen_primes()
while i < 100:
    print(next(x))
    i += 1
