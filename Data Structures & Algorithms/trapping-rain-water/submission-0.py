class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: No height
        if not height: return 0
        # Get default left and right pointers
        left, right = 0, len(height) - 1
        # Initialize the max left and right heights
        leftMax, rightMax = height[left], height[right]
        # Compute the max water trapped in height array
        rainWater = 0
        while left < right:
            if leftMax <= rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                rainWater += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                rainWater += rightMax - height[right]
        # Return the max water trapped
        return rainWater

