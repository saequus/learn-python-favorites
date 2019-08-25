# https://leetcode.com/problems/bitwise-and-of-numbers-range/


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        diff = n - m
        power = 0
        while diff > 2 ** power:
            power += 1
        return m & n & 0xFFFFFFFF << power


x = Solution()
print('The output should be 0')
print('Output:', x.rangeBitwiseAnd(5, 9))
print('The output should be 3073')
print('Output:', x.rangeBitwiseAnd(52321, 7435))
