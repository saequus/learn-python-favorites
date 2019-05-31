dividend = -26310
divisor = 341


class DivideTwoIntegers:
    def __init__(self):
        self.link = 'https://leetcode.com/problems/divide-two-integers/'
        self.description = 'Given two integers dividend and divisor, divide two integers ' \
                           'without using multiplication, division and mod operator. ' \
                           'Return the quotient after dividing dividend by divisor.' \
                           'The integer division should truncate toward zero.'

    def divide2(self, dividend, divisor):
        if divisor == 0:
            return -1
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quot = 0

        while divisor <= dividend:
            dividend -= divisor
            quot += 1
        return sign * quot

    def divide3(self, dividend, divisor):
        if divisor == 0:
            return -1

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        temp = 0

        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                quotient |= 1 << i

        return sign * quotient


f = DivideTwoIntegers()
print(f.divide2(dividend, divisor))
print(f.divide3(dividend, divisor))





