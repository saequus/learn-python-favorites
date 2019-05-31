
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
print(f.intToRoman(144))

