class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        for index, curInterval in enumerate(intervals):
            if curInterval[0] > newInterval[1]:
                newIntervals.append(newInterval)
                return newIntervals + intervals[index:]
            elif curInterval[1] < newInterval[0]:
                newIntervals.append(curInterval)
            else:
                newInterval = [min(curInterval[0], newInterval[0]), max(curInterval[1], newInterval[1])]
        newIntervals.append(newInterval)
        return newIntervals