# ============================================================================
# ========================= Make Fibonacci Generator  ========================
# ================== and Generator for Non Fibonacci numbers =================
# ============================================================================


def get_fibonacci_sequence(self):
    m = 1
    n = 1
    while True:
        temp = m
        m = m + n
        n = temp
        yield m


class GetNumsNotFibonacci:

    def getFi(self):
        m = 1
        n = 1
        while True:
            temp = m
            m = m + n
            n = temp
            yield m

    def getNotFi(self, number):
        stack = []
        res = []
        for idx, val in enumerate(self.getFi()):
            stack.append(val)
            if len(stack) >= 3:
                first = stack.pop(0)
                second = stack[0]
                for j in range(first + 1, second):
                    res.append(j)
            if idx >= number:
                break
        return res


f = GetNumsNotFibonacci()
print(f.getNotFi(12))

