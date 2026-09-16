class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Initialize a counter variable for minimum rooms
        count = 0
        # Sort (in-place) the intervals by start time
        intervals.sort(key = lambda interval: interval.start)
        # Greedily allocate rooms when none are available
        rooms = []
        # Process the intervals by end time priority
        for interval in intervals:
            # Case 1: No room is availiable 
            if not rooms or rooms[0] > interval.start:
                count += 1
                heapq.heappush(rooms, interval.end)
            # Case 2: A room is availiable
            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms, interval.end)
        return count
            

        