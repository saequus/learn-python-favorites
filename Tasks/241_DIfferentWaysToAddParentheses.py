class Solution(object):
    def comp(self, exp):
        if len(exp) == 1:
            return [int(exp[0])]

        res_list = []

        # [left] [i] [right]
        for i in range(1, len(exp), 2):
            left_list = self.comp(exp[:i])
            right_list = self.comp(exp[i + 1:])

            for l in left_list:
                for r in right_list:
                    if exp[i] == '+':
                        res_list += [l + r]
                    elif exp[i] == '-':
                        res_list += [l - r]
                    else:
                        res_list += [l * r]
        return res_list

    def diff_ways_to_compute(self, exp):
        import re
        exp = re.findall(r'(\d+|\W)', exp)
        return self.comp(exp)


# Code driver

solution = Solution()
print(solution.diff_ways_to_compute('2-1-1'))
print('To compare with: [2,0]')
print(solution.diff_ways_to_compute("2-4*3+1-5"))
print('To compare with: [6,6,-6,-9,-6,2,2,-14,-10,-19,-16,-13,-14,-10]')

