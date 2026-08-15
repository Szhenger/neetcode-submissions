class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Get an empty array of triplets
        zeroSums = []
        # Sort (in-place) the nums array of integers
        nums.sort()
        # Compute all the triplets satisfying the equation
        for i in range(len(nums) - 2):
            # Short-circuit
            if nums[i] > 0:
                break
            # Skip duplicates
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            # Two-pointer algorithm
            j, k = i + 1, len(nums) - 1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                # Case 1: curSum < 0
                if curSum < 0:
                    j += 1
                # Case 2: curSum > 0
                elif curSum > 0:
                    k -= 1
                # Case 3: curSum == 0
                else:
                    zeroSums.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # Skip duplicates
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        # Return the output array of triplets
        return zeroSums



