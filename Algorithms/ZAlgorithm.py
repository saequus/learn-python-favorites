p = "aacecaaa"
p1 = 'abcdabcdabia'


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


def zf(s):
    output = []
    if not s:
        return output
    i, slen = 1, len(s)
    output.append(slen)
    while i < slen:
        left, right = 0, i
        while right < slen and s[left] == s[right]:
            left += 1
            right += 1
        output.append(left)
        i += 1
    return output


print(naive_z(p))
print(naive_z(p1))

# print(naive_z('asdfjm asdfjdm asdfnd s amdmms a asdfd'))

print(' - - - - ')
fs = 'Все о том же поет луна. Мне причудилось удивительное событие'
fss = 'Мне при'

print(zf(p))
print(zf(p1))
g = (str(fss + '^' + fs))
t = zf(g)
print(t)




