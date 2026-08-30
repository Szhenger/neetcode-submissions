class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        space, stack = [], []
        def backtrack(openN: int, closedN: int) -> None:
            if openN == n == closedN:
                space.append("".join(stack))
                return None
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            if openN > closedN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return space


