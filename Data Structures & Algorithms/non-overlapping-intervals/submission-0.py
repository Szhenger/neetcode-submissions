class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        minInt = 0
        intervals.sort(key = lambda interval: interval[0])
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                minInt += 1
                prevEnd = min(prevEnd, end)
        return minInt
            