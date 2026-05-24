class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Get an empty array of zero-sum triplets 
        sums = []
        # Sort (in-place) the input nums array in non-decreasing order
        nums.sort()
        # Iterate over the sorted nums array
        for i in range(len(nums) - 2):
            # Short-circuit the postive triplets
            if nums[i] > 0:
                break
            # Skip duplicate the zero-sum triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Find all the zero-sum [nums[i], nums[j], nums[k]] triplets
            j, k = i + 1, len(nums) - 1
            while j < k:
                zeroSum = nums[i] + nums[j] + nums[k]
                if zeroSum < 0:
                    j += 1
                elif zeroSum > 0:
                    k -= 1
                else:
                    sums.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return sums


