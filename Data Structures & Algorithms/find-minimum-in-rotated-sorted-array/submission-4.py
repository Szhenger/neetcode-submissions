class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Get a default minimum variable
        minNum = float('inf')
        # Binary search on the rotated sorted nums array
        left, right = 0, len(nums) - 1
        while left <= right:
            # Compute the middle index
            middle = (left + right) // 2
            # Case 1: middle is in sorted LEFT subarray
            if nums[left] <= nums[middle]:
                minNum = min(minNum, nums[left])
                left = middle + 1
            # Case 2: middle is in sorted RIGHT subarray
            else:
                minNum = min(minNum, nums[middle])
                right = middle - 1
        return minNum

