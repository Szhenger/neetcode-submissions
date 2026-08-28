class Solution:
    def findMin(self, nums: List[int]) -> int:
        minInt = float('inf')
        lef, rig = 0, len(nums) - 1
        while lef <= rig:
            mid = (lef + rig) // 2
            if nums[lef] <= nums[mid]:
                minInt = min(minInt, nums[lef])
                lef = mid + 1
            else:
                minInt = min(minInt, nums[mid])
                rig = mid - 1
        return minInt