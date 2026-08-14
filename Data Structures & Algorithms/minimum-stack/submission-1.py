class MinStack:

    def __init__(self) -> None:
        # Initialize the order and stack lists
        self.order = [float('inf')]
        self.stack = []

    def push(self, val: int) -> None:
        # Push the input value onto the stack list
        if self.order and self.order[-1] >= val:
            self.order.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        # Remove the top value off the stack list
        if self.order and self.order[-1] == self.stack[-1]:
            self.order.pop()
        self.stack.pop()

    def top(self) -> int:
        # Get the top value off the stack list
        return self.stack[-1]


    def getMin(self) -> int:
        # Return the minimum value in the stack list
        return self.order[-1]