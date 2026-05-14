class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty hashmap
        numMap = {} # num : idx
        # Enumerate over (idx, num) in nums
        for i, num in enumerate(nums):
            # Compute the complement of num
            com = target - num
            # Search for the complement in numMap
            if com in numMap:
                # Return the match
                return [numMap[com], i]
            # Else map num to idx
            numMap[num] = i 