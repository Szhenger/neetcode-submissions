class Solution:
    def longestConsecutive(self, nums: List[int]):
        # Get the hashset of unique integers 
        numSet = set(nums)
        # Find the longest consecutive sequence
        longest = 0
        for num in numSet:
            # Build the local consecutive sequence
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                # Calculate the global max length
                longest = max(longest, length)
        return longest
