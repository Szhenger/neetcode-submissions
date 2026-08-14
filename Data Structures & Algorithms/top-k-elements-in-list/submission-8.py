class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get the integer counts of the nums array
        counts = Counter(nums) # num -> cnt
        # Heapify the counts dictionary
        maxHeap = []
        for num, cnt in counts.items():
            maxHeap.append((cnt, num))
        heapq.heapify_max(maxHeap)
        # Return the k most frequent elements
        kFreqs = []
        for _ in range(k):
            cnt, num = heapq.heappop_max(maxHeap)
            kFreqs.append(num)
        return kFreqs


