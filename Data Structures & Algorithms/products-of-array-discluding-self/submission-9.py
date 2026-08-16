class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize a Python array of integers
        output = len(nums) * [None]
        # Prefix sum algorithm
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        # Suffix sum algorithm
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        # Return the Python array of products
        return output
        