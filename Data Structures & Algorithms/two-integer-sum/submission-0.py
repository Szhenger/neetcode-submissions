class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i, num in enumerate(nums):
            com = target - num
            if com in numsMap:
                return [numsMap[com], i]
            numsMap[num] = i