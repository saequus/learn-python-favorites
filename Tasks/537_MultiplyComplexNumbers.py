# https://leetcode.com/problems/complex-number-multiplication


def complex_number_multiply(a: str, b: str) -> str:
    fr, fm = a.split('+')
    fm = fm.rstrip('i')

    sr, sm = b.split('+')
    sm = sm.rstrip('i')

    part1 = int(fr) * int(sr) - int(fm) * int(sm)
    part2 = int(fr) * int(sm) + int(fm) * int(sr)
    return str(part1) + '+' + str(part2) + 'i'


# Test


first = "19+-1i"
second = "10+-5i"
res = complex_number_multiply(first, second)
print('Compare: ', res, ' and 185+-105i')
