class Solution(object):
    def __init__(self):
        self.letters = {1: [], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
                        6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        if not digits:
            return []
        res = []
        line = []
        self.helper(digits, 0, res, line)
        return res

    def helper(self, digits, cur, res, line):

        if len(line) == len(digits):
            res.append(''.join([x for x in line]))
            return

        for l in self.letters[int(digits[cur])]:
            line.append(l)
            self.helper(digits, cur + 1, res, line)
            line.pop()


t = '23'
f = Solution()
print(f.letterCombinations(t))
