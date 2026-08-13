class Solution:
    def isValid(self, s: str) -> bool:
        # Get an empty Python stack of open brackets
        openStack = []
        # Map a Python dictionary of closed -> open brackets
        closedMap = { 
            ')' : '(', '}' : '{', ']' : '[' 
        }
        # Iterate over the Python str of brackets
        for c in s:
            # Case 1: c is a closed bracket
            if c in closedMap:
                if openStack and openStack[-1] == closedMap[c]:
                    openStack.pop()
                else:
                    return False
            # Case 2: c is an open bracket
            else:
                openStack.append(c)
        # Return the state of Python stack
        return not openStack
