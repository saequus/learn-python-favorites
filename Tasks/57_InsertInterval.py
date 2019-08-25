class Solution:
    @staticmethod
    def insert_interval(intervals: list, newInterval: list) -> list:
        if not intervals:
            return [newInterval]
        i = 0
        while i < len(intervals) and newInterval[0] >= intervals[i][0]:
            i += 1
        intervals.insert(i, newInterval)
        start = i
        if start != 0:
            start -= 1

        for i in range(start, len(intervals) - 1):
            j = i + 1
            while j < len(intervals) and intervals[i][1] >= intervals[j][0]:
                if intervals[i][1] < intervals[j][1]:
                    intervals[i][1] = intervals[j][1]
                del intervals[j]
        return intervals


x = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
y = [4, 8]
u = Solution()
print(u.insert_interval(x, y))


x = [[1,3],[6,9]]
y = [2,5]
u = Solution()
print(u.insert_interval(x, y))

