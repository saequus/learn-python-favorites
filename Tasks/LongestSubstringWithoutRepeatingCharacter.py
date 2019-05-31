

sg = "abcabcbb"
sr = "b.asfb."
st = "v_v521.v"
sy = "010171"
sv = "_a_bca90bcbb"
sh = "**jkl;_qw_er_u_iop"

def asdf(s):
    s = list(s)
    stack = []
    memory = []
    for i in range(len(s)):
        if s[i] not in stack:
            stack.append(s[i])
        else:
            ind = stack.index(s[i])
            if len(stack) > len(memory):
                memory = stack
            stack = stack[ind + 1:]
            stack.append(s[i])
    if len(stack) > len(memory):
        memory = stack
    return len(memory)


print(asdf(sg))
print(asdf(sr))
print(asdf(st))
print(asdf(sy))
print(asdf(sv), 6)
print(asdf(sh), 8)