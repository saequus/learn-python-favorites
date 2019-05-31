x = 6
y = 7


s2 = '11'
s3 = '21'
s4 = "1211"
s5 = "111221"
s6 = "312211"


class Solution(object):

    def countAndSay(self, n):
        res = '1'
        for i in range(n + 1):
            res = self.nextNumber(res)
        return res


    def nextNumber(self, s):
        res = []
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            res += str(count) + s[i]
            i += 1
        return ''.join(str(i) for i in res)


f = Solution()
print(f.countAndSay(5))
print(f.nextNumber('111221'))
# print(f.countAndSay(y))


