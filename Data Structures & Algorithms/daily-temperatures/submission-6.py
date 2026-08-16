class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize a Python array of integers
        result = len(temperatures) * [0]
        # Get an empty stack of (day, tmp) tuples
        stack = []
        # Enumerate the Python array of temperatures
        for day, tmp in enumerate(temperatures):
            while stack and stack[-1][1] < tmp:
                pre, dum = stack.pop()
                result[pre] = day - pre
            stack.append((day, tmp))
        # Return the Python array of differences
        return result