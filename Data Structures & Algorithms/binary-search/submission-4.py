class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Get the default pointers
        left, right = 0, len(nums) - 1
        # Search for target between the pointers 
        while left <= right:
            # Compute the index between the pointers
            middle = (left + right) // 2
            # Case 1: target is greater than value
            if nums[middle] < target:
                left = middle + 1
            # Case 2: target is less than value
            elif nums[middle] > target:
                right = middle - 1
            # Case 3: target is equal to value
            else:
                return middle
        # Case 4: target doe not exist between the pointers
        return -1






