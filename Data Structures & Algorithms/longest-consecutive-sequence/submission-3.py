class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Search for the maximal length
        maxLen, numSet = 0, set(nums)
        for num in numSet:
            if num - 1 not in numSet:
                curLen = 0
                while num + curLen in numSet:
                    curLen += 1
                maxLen = max(maxLen, curLen)
        return maxLen
                
            
