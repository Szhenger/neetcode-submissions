class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        minInt = 0
        intervals.sort(key = lambda interval: interval[0])
        preEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < preEnd:
                minInt += 1
                preEnd = min(preEnd, end)
            else:
                preEnd = end
        return minInt
            