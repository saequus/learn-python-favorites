
res = []
n = 0
x = ['sfents', 'sfg', 'sfgen', 'sfenam']
y = ["flower","flow","flight"]
stack = x[0]
iterator = 0

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs or len(strs) == 0:
            return ""
        prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix


f = Solution()
print(f.longestCommonPrefix(y))
