class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort (in-place) the intervals by start time
        intervals.sort(key = lambda interval: interval.start)
        # Compare the intervals pair-wise for potential conflicts
        for i in range(len(intervals) - 1):
            # Short-circuit (conflict found)
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True
