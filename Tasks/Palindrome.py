
# def dsf(x):
#     res = 0
#     x = str(x)
#     if len(x) == 1:
#         return True
#     for i in range(len(x) // 2):
#         print(len(x), i, '777')
#         if x[i] == x[len(x)-i-1]:
#             print(x[i], x[len(x)-i-1])
#             res = 0
#         else:
#             res = 1
#     return True if res == 0 else False

def dsf(x):
    temp = int(x)
    rev = 0
    if temp < 0:
        return False
    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10
    if temp == rev:
        return True
    else:
        return False


print(dsf(12000021), dsf(202), dsf(-12321), dsf(78987), dsf(12321))
