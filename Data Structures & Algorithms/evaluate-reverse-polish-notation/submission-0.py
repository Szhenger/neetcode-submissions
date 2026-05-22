class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Get an empty stack of integers
        stack = []
        # Iterate over the tokens list
        for token in tokens:
            if token == '+':
                x, y = stack.pop(), stack.pop()
                stack.append(x + y)
            elif token == '-':
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif token == '*':
                x, y = stack.pop(), stack.pop()
                stack.append(x * y)
            elif token == '/':
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(token))
        # Return the state of computation
        return stack[0]
