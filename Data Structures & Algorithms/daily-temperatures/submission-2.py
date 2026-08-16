class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize a Python array of integers
        result = len(temperatures) * [0]
        # Get an empty stack of (day, tmp) tuples
        stack = []
        # Enumerate the Python array of temperatures
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j, dummy = stack.pop()
                result[j] = i - j
            stack.append((i, temp))
        # Return the Python array of differences
        return result