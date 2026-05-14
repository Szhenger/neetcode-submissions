class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty hashset
        numSet = set()
        # Iterate over the input array
        for num in nums:
            # If num in numSet, we found duplicate 
            if num in numSet:
                return True
            # Else add num to numSet
            else:
                numSet.add(num)
        # No duplicate exists
        return False