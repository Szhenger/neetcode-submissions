class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the number of occurances
        counts = Counter(nums) # num -> cnt
        # Populate the buckets array
        buckets = [[] for _ in range(len(nums) + 1)] # idx -> cnt
        for num, cnt in counts.items():
            buckets[cnt].append(num)
        # Find the top k most frequent elements
        results = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results


        
