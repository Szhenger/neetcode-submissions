class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        newIntervals = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > newIntervals[-1][1]:
                newIntervals.append(interval)
            else:
                newIntervals[-1][1] = max(newIntervals[-1][1], interval[1])
        return newIntervals

