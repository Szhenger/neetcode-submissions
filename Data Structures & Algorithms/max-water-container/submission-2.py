class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize a global maximal water variable
        maxWater = 0
        # Greedily search the input heights array 
        left, right = 0, len(heights) - 1
        while left < right:
            # Compute the local maximal water
            maxWater = max(maxWater, min(heights[left], heights[right]) * (right - left))
            # Update the bar pointers
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        # Return the global maximal water variable
        return maxWater