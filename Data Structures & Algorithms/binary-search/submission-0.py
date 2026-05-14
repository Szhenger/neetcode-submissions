class Solution:
    def search(self, nums: List[int], target) -> int:
        # Initialize two-pointer approach
        lef, rig = 0, len(nums) - 1
        # Loop invariant left < right pointer
        while lef <= rig:
            # Compute the middle index
            mid = (lef + rig) // 2
            # Check if middle value is target
            if nums[mid] == target:
                return mid
            # Else if the target must be to the right of middle index
            elif nums[mid] < target:
                lef = mid + 1
            # Else the target must be to the left of the middle index
            else:
                rig = mid - 1
        # Target does not exist in input array nums
        return -1