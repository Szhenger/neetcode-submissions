class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Get an empty Python stack of integers
        stack = []
        # Evaluate the arithmetic expression
        for token in tokens:
            # Case 1: token == +
            if token == '+':
                x, y = stack.pop(), stack.pop()
                stack.append(x + y)
            # Case 2: token == -
            elif token == '-':
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            # Case 3: token == *
            elif token == '*':
                x, y = stack.pop(), stack.pop()
                stack.append(x * y) 
            # Case 4: token == /
            elif token == '/':
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            # Case 5: token == int
            else:
                stack.append(int(token))
        return stack[0]
            