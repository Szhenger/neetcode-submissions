class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get an default list of integers
        output = [1] * len(nums)
        # Compute the prefix products
        prefix = 1
        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]
        # Compute the suffix products
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        # Return the correct output
        return output
