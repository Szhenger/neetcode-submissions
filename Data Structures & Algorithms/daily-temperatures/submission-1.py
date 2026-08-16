class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize a Python array of integers
        result = len(temperatures) * [0]
        # Get an empty stack of (tmp, day) tuples
        stack = []
        # Enumerate the Python array of temperatures
        for day, tmp in enumerate(temperatures):
            while stack and stack[-1][0] < tmp:
                old, pre = stack.pop()
                result[pre] = day - pre
            stack.append((tmp, day))
        return result