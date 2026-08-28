class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = x * x + y * y
            minHeap.append((dist, x, y))
        heapq.heapify(minHeap)
        minList = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            minList.append([x, y])
        return minList