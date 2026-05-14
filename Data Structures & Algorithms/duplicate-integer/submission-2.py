class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Get an empty hashset
        numSet = set()
        # Iterate over the input array  
        for num in nums:
            # Short-circuit if duplicate
            if num in numSet:
                return True
            numSet.add(num)
        # Return input array is unique
        return False
