class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the number of occurances
        counts = Counter(nums) # num -> cnt
        # Populate the max heap with the count priority 
        maxHeap = []
        for num, count in counts.items():
            maxHeap.append((count, num))
        # Heapify the max heap
        heapq.heapify_max(maxHeap)
        # Populate the topK array
        topK = []
        for _ in range(k):
            count, num = heapq.heappop_max(maxHeap)
            topK.append(num)
        return topK
        
