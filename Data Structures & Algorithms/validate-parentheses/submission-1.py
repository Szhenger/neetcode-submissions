class Solution:
    def isValid(self, s: str) -> bool:
        # Get an empty stack of open brackets
        openStack = []
        # Map closed brackets to open brackets
        closedMap = {
            ')' : '(', '}' : '{', ']' : '[' 
        }
        # Iterate over the input string
        for c in s:
            # Case 1: c is closed
            if c in closedMap:
                # Subcase 1: Recursively close brackets
                if openStack and openStack[-1] == closedMap[c]:
                    openStack.pop()
                # Subcase 2: Short-circuit if invalid
                else:
                    return False
            # Case 2: c is open
            else:
                openStack.append(c)
        # Return the state of stack
        return not openStack
