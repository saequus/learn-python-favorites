y = [1, 2, 0, -1, -2]   # [[-2, 0, 2], [-1, 0, 1]]
x = [-1, 0, 1, 2, -1, -4]   # [[-1, -1, 2], [-1, 0, 1]]
t = [-1, 0, -3, 7, 3, -6, -9, 4, -4, 2, -1, -4]  # [[-9, 2, 7], [-6, 2, 4], [-1, -1, 2]]

#
# class Solution(object):
#     def threeSum(self, nums):
#         if len(nums) < 3:
#             return []
#
#         nums = sorted(nums)
#         triplets = []
#         for i in range(len(nums) - 2):
#             j = i + 1
#             k = len(nums) - 1
#             while j < k:
#                 currSum = nums[i] + nums[j] + nums[k]
#                 if currSum == 0:
#                     tmpList = sorted([nums[i], nums[j], nums[k]])
#                     if tmpList not in triplets:
#                         triplets.append(tmpList)
#                     j += 1
#                 elif currSum > 0:
#                     k -= 1
#                 elif currSum < 0:
#                     j += 1
#         return triplets


# class Solution(object):
#     def threeSum(self, s):
#         conset = set()
#         for i in range(len(s) - 2):
#             for j in range(1, len(s) - 1):
#                 for k in range(2, len(s)):
#                     a = s[i]
#                     b = s[j]
#                     c = s[k]
#                     if a + b + c == 0:
#                         conset.add((a, b, c))
#         return list(conset)



class Solution(object):
    def threeSum(self, nums):

        n = len(nums)
        res = set()

        nums.sort()

        if n < 3:
            return []

        for i in range(n - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                j = i + 1
                k = n - 1

                while j < k:
                    sum_ = nums[i] + nums[j] + nums[k]

                    if sum_ == 0:
                        res.add((nums[i], nums[j], nums[k]))
                        j += 1
                        k -= 1
                    elif sum_ < 0:
                        j += 1
                    else:
                        k -= 1

        return list(res)




f = Solution()
print(f.threeSum(x))


# s = [[1, 1], ['1', '0']]
# print(s.index(['1, 0]))