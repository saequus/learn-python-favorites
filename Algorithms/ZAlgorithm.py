p = 'aacecaaa'
p1 = 'abcdabcdabi'


def zfun(s):
    out = []
    if not s:
        return out
    i, slen = 1, len(s)
    out.append(slen)
    while i < slen:
        left, right = 0, i
        while right < slen and s[left] == s[right]:
            left += 1
            right += 1
        out.append(left)
        i += 1
    return out


print(zfun(p))
print(zfun(p1))


def naive_z(string):
    n = len(string)
    z = [n]

    for i in range(1, n):
        L = R = i
        while R < n and string[R - L] == string[R]:
            R += 1
        z.append(R - L)
    return z


fs = 'Все о том же поет луна. Все о том же'
fss = 'мне причем мне не очень'

x1 = zfun(fs)
print(x1)
x2 = zfun(fss)
print(x2)


