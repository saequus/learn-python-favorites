# Get initial reminder and quotient. Check whether quotient >= 1. If so, tokes

# Task 948

# class Solution(object):
#     def bagOfTokensScore(self, tokens, P):
#         """
#         :type tokens: List[int]
#         :type P: int
#         :rtype: int
#         """
#         total = 0
#         i = 0
#         tokens = sorted(tokens)
#         while tokens and P // tokens[i] >= 1:
#             total += 1
#             P -= tokens[i] * 1
#             tokens.pop(i)
#         return total
#
#
# n = [100, 200, 400, 600, 700, 400, 50, 1200]
#
# f = Solution()
# print(f.bagOfTokensScore(n, 1000))



# f = Solution()
# print(f.bagOfTokensScore(n, 200))