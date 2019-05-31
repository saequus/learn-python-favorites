


s = 'saedjendnxe'

for index, value in enumerate(s):
    if value == 'e':
        print('good', index, value)

opening_brackets = ['(', '[', '{']
brackets_map = {')': '(', ']': '[', '}': '{'}
exee = '({})[](())'

class Solution(object):
    def isValid(self, s):
        if not s:
            return True

        if s[0] not in opening_brackets:
            return False

        stack = []
        for index, bracket in enumerate(s):
            if bracket in opening_brackets:
                stack.append(bracket)
            if bracket not in opening_brackets:
                try:
                    last_opening_bracket = stack.pop()
                    if last_opening_bracket != brackets_map[bracket]:
                        return False
                except IndexError:
                    return False

        return not stack


f = Solution()
print(f.isValid(exee))
