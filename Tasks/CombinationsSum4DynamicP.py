class GetComninationSum4:
    def __init__(self):
        self.link = 'https://leetcode.com/problems/combination-sum-iv/'
        self.description = 'Given an integer array with all positive ' \
                           'numbers and no duplicates, find the number of ' \
                           'possible combinations that add up to a ' \
                           'positive integer target.'

    @staticmethod
    def get_combination_sum_4(nums, target):
        nums = sorted(nums)
        combs = [1] + [0] * target
        for i in range(target+1):
            for n in nums:
                if n < i:
                    combs[i] += combs[i - n]
                else:
                    combs[i] += n == i
                    break
        print(combs)
        return combs[target]


numbers = [1, 2, 3]
c = GetComninationSum4
print(c.get_combination_sum_4(numbers, 4))


