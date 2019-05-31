x1 = [1,2,3,1,1, 4]
k1 = 1
t1 = 2

x2 = [1,5,9,1,5,9]
x3 = 1,5,9,1,5,9
k2 = 2
t2 = 3


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):

        if k <= 0 or t < 0 or len(nums) < 2:
            return False

        min_val = min(nums)
        if min_val < 0:
            nums = [n - min_val for n in nums]
            min_val = 0
        max_val = max(nums)
        bucket = {}
        for i, num in enumerate(nums):
            print(bucket)
            idx = num // (t + 1)
            if len(bucket) == k + 1:
                bucket.pop(nums[i - k - 1] // (t + 1))
            if idx in bucket:
                return True
            elif idx - 1 in bucket and num - bucket[idx - 1] <= t:
                return True
            elif idx + 1 in bucket and bucket[idx + 1] - num <= t:
                return True
            else:
                bucket[idx] = num

        return False


f = Solution()
print(f.containsNearbyAlmostDuplicate(x1, k1, t1))
