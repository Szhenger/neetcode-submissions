class Solution:
    def rob(self, nums: List[int]) -> int:
        def ROB(nums: List[int]) -> int:
            rob0 = rob1 = 0
            for num in nums:
                rob0, rob1 = rob1, max(rob0 + num, rob1)
            return rob1
        return max(nums[0], ROB(nums[1:]), ROB(nums[:-1]))