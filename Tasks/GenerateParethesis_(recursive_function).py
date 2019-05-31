


class Solution(object):
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n):
        res = self.res
        s = list(2 * n * [''])
        if n > 0:
            self._resolveParenthesis(s, 0, n, 0, 0)
            return res

    def _resolveParenthesis(self, s, pos, n, open, close):
        res = self.res
        if close == n:
            res.append("".join(str(i) for i in s))
            return

        else:
            if open < n:
                s[pos] = '('
                self._resolveParenthesis(s, pos + 1, n, open + 1, close)
            if close < open:
                s[pos] = ')'
                self._resolveParenthesis(s, pos + 1, n, open, close + 1)


f = Solution()
print(f.generateParenthesis(4))


# another approach
#
# class Solution(object):
#     def generateParenthesis(self, n):
#         if n == 0: return ['']
#         ans = []
#         for c in range(n):
#             for left in self.generateParenthesis(c):
#                 for right in self.generateParenthesis(n-1-c):
#                     ans.append('({}){}'.format(left, right))
#         return ans
#
#
#
# f = Solution()
# print(f.generateParenthesis(3))