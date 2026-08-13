class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Get an empty Python hashmap of num -> idx
        maps = {} 
        # Enumerate over the input Python list of integers
        for idx, num in enumerate(nums):
            # Get the complement of num
            com = target - num
            # Search for complement
            if com in maps:
                return [maps[com], idx]
            # Insert (num, idx) into the Python hashmap
            maps[num] = idx
        
