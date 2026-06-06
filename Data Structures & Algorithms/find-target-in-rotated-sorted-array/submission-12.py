class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search on the rotated sorted array
        left, right = 0, len(nums) - 1
        while left <= right: 
            # Get the middle index in the rotated sorted subarray
            middle = (left + right) // 2
            # Case 1: middle is the target index
            if nums[middle] == target:
                return middle
            # Case 2: middle is in the LEFT sorted subarray
            elif nums[left] <= nums[middle]:
                if nums[left] > target or nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            # Case 3: middle is in the RIGHT sorted subarray
            else:
                if nums[middle] > target or nums[right] < target:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1
