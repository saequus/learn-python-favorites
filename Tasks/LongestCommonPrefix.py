x = ["flower", "flow", "flight"]


# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         length = len(min(strs))
#         stack = str()
#         for i in range(length):
#             let = list(strs[0])[i]
#             for j in range(len(strs)):
#                 word = list(strs[j])
#                 if word[i] == let:
#                     stack += let
#
#         return stack
#
#
# f = Solution()
# print(f.longestCommonPrefix(x))



class Solution(object):
    def longestCommonPrefix(self, strs):
        length = len(list(min(strs)))
        word = list(min(strs))
        stack = str()
        for letter in range(length):
            for i in range(len(strs)):
                word2 = list(strs[i])
                if word[letter] == word2[letter]:
                    stack += word[letter]
        return stack


g = Solution()
print(g.longestCommonPrefix(x))

print(x[0])

# letter = str(list(x[0])[:2])
# print(letter)