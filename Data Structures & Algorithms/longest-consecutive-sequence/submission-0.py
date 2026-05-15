class Solution:
    def longestConsecutive(self, nums: List[int]):
        # Get the hashset of unique integers 
        numSet = set(nums)
        # Find the longest consecutive sequence
        longest = 0
        # Iterate over the hashset
        for num in numSet:
            # Build a consecutive sequence of unique integers
            length = 1
            while num + 1 in numSet:
                length += 1
                num += 1
            # Calculate the global max length
            longest = max(longest, length)
        return longest
