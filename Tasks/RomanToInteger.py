
class Roman:
    def intToRoman(self, n):
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
             9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        stack = str()
        for number, value in d.items():
            if n // number > 0:
                total = n // number
                n %= number
                stack += total * value
        return stack


f = Roman()
print(f.intToRoman(888))




class Solution:
    def romanToInt(self, s):
        self.keys = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
        self.to_arabic = {'IV': '4', 'IX': '9', 'XL': '40', 'XC': '90', 'CD': '400', 'CM': '900',
                          'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}
        for key in self.keys:
            if key in s:
                s = s.replace(key, ' {}'.format(self.to_arabic.get(key)))
        arabic = sum(int(num) for num in s.split())
        return arabic


ver = 'DCCCLXXVI'

s = Solution()
print(s.romanToInt(ver))