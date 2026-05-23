class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Get a default array of warmers days
        result = [0] * len(temperatures)
        # Process each (day, temp) in a stack
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j, dummy = stack.pop()
                result[j] = i - j
            stack.append((i, temp))
        # Return the state of computation
        return result
