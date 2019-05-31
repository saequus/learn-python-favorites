class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        h = [0] * (len(citations) + 1)
        print(h)
        for i in citations:
            if i > len(citations):
                h[-1] += 1
            else:
                h[i] += 1
        print(h)
        sum_c = 0
        for i, j in enumerate(h[::-1]):
            sum_c += j
            if sum_c >= len(citations) - i:
                return len(citations) - i
        return 0





citations = [3,0,6,1,5]
# 3
citations2 = [3,2,6,1,5,8, 6, 10, 1]
# 5
citations3 = [3,0,6,1,0,2]
# 2
f = Solution()
print(f.hIndex(citations2))
