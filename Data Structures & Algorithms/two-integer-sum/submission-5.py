class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Get an empty hashmap
        numMap = {} # num -> idx
        # Enumerate over the input array
        for i, num in enumerate(nums):
            # Get the complement
            com = target - num
            # Find the complement in the hashmap
            if com in numMap:
                return [numMap[com], i]
            # Memoize (num, idx) key-value pair in the hashmap
            numMap[num] = i
        