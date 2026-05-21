class MinStack:

    def __init__(self):
        # Initialize a default stack of min vals
        self.localMin = [float('inf')]
        # Initialize a empty stack of input vals
        self.minStack = []

    def push(self, val: int) -> None:
        # Input val is global min
        if self.localMin and self.localMin[-1] >= val:
            self.localMin.append(val)
        # Append val to stack instance
        self.minStack.append(val)

    def pop(self) -> None:
        # Top val is global min
        if self.localMin and self.localMin[-1] == self.minStack[-1]:
            self.localMin.pop()
        # Remove the val from stack instance 
        self.minStack.pop()

    def top(self) -> int:
        # Return the top val in the stack instance
        return self.minStack[-1]

    def getMin(self) -> int:
        # Return the minimum element in the stack instance
        return self.localMin[-1]
        
