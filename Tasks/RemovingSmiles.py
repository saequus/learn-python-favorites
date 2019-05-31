def find_divider(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
            print(a)
        else:
            b = b % a
            print(b)

    return a + b, a, b


print(find_divider(180, 130))


x = 14
n = ''
while x > 0:
    y = str(x % 2)
    n = y + n
    x = int(x / 2)

print(n)

a = "What:-((is this city?:-)) :-))) I've never been here:-)))()( It's very nice!"


def rem(l):
    print(len(l))
    r = ""
    i = 0
    while i < len(l):
        if l[i] == ":":
            if l[i+1] == '-':
                if l[i+2] == ')' or l[i+2] == '(':
                    i += 3
                while l[i] == '(' or l[i] == ')':
                    i += 1
                continue
        else:
            if i < len(l):
                r += l[i]
                print(r)
                i += 1
    return r


print(rem(a))
