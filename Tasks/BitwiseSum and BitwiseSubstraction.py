def get_sum(a, b):
    if a == -b:
        return 0
    if a < 0:
        return -get_sum(-a, -b)
    if a < b:
        a, b = b, a
    while b:
        borrow = a & b
        a ^= b
        b = borrow << 1
    return a

def get_substact(a, b):
    while b:
        borrow = (~a) & b
        a ^= b
        b = borrow << 1
    return a


print(get_sum(-4, 13))
print(get_substact(-4, 13))