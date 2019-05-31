
# – – – – – – –  – – – – – – –  – – – – – – –
# n1 = [3, 5, 1]
# n2 = [2, 1, 4]
#
#
# class PopularObject:
#
#     def uniuni(self, l1, l2):
#         l3 = int(''.join(str(l1[i])for i in range(len(l1)))) + int(''.join(str(l2[j])for j in range(len(l2))))
#         lfi = [int(i) for i in str(l3)]
#         return lfi
#
#
# f = PopularObject()
# print(f.uniuni(n1, n2))
# – – – – – – –  – – – – – – –  – – – – – – –
# s = 'abcabcabb'
#
#
# class StringClassifier:
#
#     def longest_sbsqnce(self, st):
#         arr, stack = list(), list()
#         for i in st:
#             if i in arr:
#                 if len(arr) > len(stack):
#                     stack = arr
#                 arr = list()
#             else:
#                 arr.append(i)
#
#
#         return len(stack)
#
#
# f = StringClassifier()
# print(f.longest_sbsqnce(s))
# – – – – – – –  – – – – – – –  – – – – – – –
#
# nums1 = [1, 3]
# nums2 = [2]
# # 2
#
# nums3 = [1, 2]
# nums4 = [3, 4]
# # 2.5
#
# nums5 = [1, 2, 5, 6]
# nums6 = [3, 4, 7, 8]
# # 4.5
#
#
# class Better:
#
#     def medimedi(self, arr1, arr2):
#         pos1 = len(arr1) // 2
#         pos2 = len(arr2) // 2
#         return (arr1[pos1] + arr2[pos2]) / 2
#
#     def medi(self, arr1, arr2):
#         arr3 = sorted(arr1 + arr2)
#         res = 0
#         if len(arr3) % 2 == 1:
#             res = arr3[int(len(arr3)//2)]
#         elif len(arr3) % 2 == 0:
#             res = (arr3[len(arr3)//2-1] + arr3[len(arr3)//2])/2
#         return res
#
#
# g = Better()
# print(g.medi(nums1, nums2))
# print(g.medi(nums3, nums4))
# print(g.medi(nums5, nums6))
#
# – – – – – – –  – – – – – – –  – – – – – – –
#
# ter = 'ghsmewertrewadmf'
# def ewn(s):
#     max_length = 1
#     length = len(s)
#     start = 0
#     for i in range(length):
#         high = i + 1
#         low = i - 1
#         while low >= 0 and high < length and s[low] == s[high]:
#             if high - low > max_length:
#                 max_length = high - low + 1
#                 start = low
#             low -= 1
#             high += 1
#     print(s[start:start+max_length])
#
# print(ewn(ter))
#
# – – – – – – –  – – – – – – –  – – – – – – –
#
#
# g = 1204900
# f = 431
# h = -453
#
# def re(n):
#     res = list()
#     d = 0
#     neg = 0
#     n = int(n)
#     if n < 0:
#         n *= -1
#         neg = 1
#     while n % 10 == 0:
#         n /= 10
#     n = list(str(int(n)))
#     for i in range(len(n)):
#         res.append(n[-i - 1])
#     res = ''.join(str(res[j]) for j in range(len(n)))
#     res = int(res)
#     if neg == 1:
#         res *= -1
#
#     return 'Reversed number is %d' %res
#
#
# print(re(h), re(f), re(g))
#
# – – – – – – –  – – – – – – –  – – – – – – –

s = '-232-n-34'

print('_'.isdecimal())

#
# negative = False
#         stack = str()
#         splitted = s.split()[0]
#         if splitted.startswith('-'):
#             negative = True
#             splitted = list(splitted)
#             splitted.pop(0)
#         for i in range(len(list(splitted))):
#
#             element = str(splitted[i])
#             if element.isdigit():
#                 stack += element
#             elif element.isalpha():
#                 if len(stack) == 0:
#                     return 0
#                 break
#         if int(stack) > 2147483648:
#             return -2147483648 if negative else 2147483647
#         return int(stack) * -1 if negative else int(stack)


f = '  sk'
print(f.isspace())
