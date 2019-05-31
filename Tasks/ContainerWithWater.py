

def sfm(arr):
    stack = arr
    sq = 1
    while stack:
        m = (fd.index(max(stack)))
        ind = stack.index(stack[m])
        print(m)
        for i in range(len(stack)):
            if (ind - stack.index(i)) * i > sq:
                sq = (ind - stack.index(i)) * i
            elif (stack.index(i) - ind) * i > sq:
                sq = (stack.index(i) - ind) * i
        stack.pop(m)
    return stack, sq


fd = [1, 3, 2, 6, 7, 1, 5]
print(sfm(fd))


