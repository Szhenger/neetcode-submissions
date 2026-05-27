class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize an area variable and stack of (index, height) pairs
        area, stack = 0, []
        # Compute the max area in the input list
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                start = index
            stack.append((start, h))
        # Compute the max area in the stack list
        for i, h in stack:
            area = max(area, h * (len(heights) - i))
        # Return the max area
        return area