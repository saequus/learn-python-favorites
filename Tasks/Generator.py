# def gen():
#     value = 1
#     while True:
#         yield value
#         value *= 2


# for idx, val in enumerate(gen()):
#     print(val)
#     if idx > 10:
#         break

#
# def getFi(self):
#     m = 1
#     n = 1
#     while True:
#         temp = m
#         m = m + n
#         n = temp
#         yield m


# class GetNumsNotFibonacci:
#
#     def getFi(self):
#         m = 1
#         n = 1
#         while True:
#             temp = m
#             m = m + n
#             n = temp
#             yield m
#
#     def getNotFi(self, number):
#         stack = []
#         res = []
#         for idx, val in enumerate(self.getFi()):
#             stack.append(val)
#             if len(stack) >= 3:
#                 first = stack.pop(0)
#                 second = stack[0]
#                 for j in range(first + 1, second):
#                     res.append(j)
#             if idx >= number:
#                 break
#         return res
#
# f = GetNumsNotFibonacci()
# print(f.getNotFi(12))


class returnNotFibonacci():
    def get(self):
        while True:
            idx, i = self.returnFi()
            temp = i


    def returnFi(self):
        m = 2
        n = 1
        while True:
            temp = m
            m = n + m
            n = temp
            yield n


# 2, 3, 5, 8, 13

    # while temp < m:
    #     yield temp


f = returnNotFibonacci()
for idx, val in enumerate(f.get()):
    print(val)
    if idx > 12:
        break

print('––––––––––––––––––––––––––––––––')

for idx, val in enumerate(f.returnFi()):
    print(val)
    if idx > 12:
        break