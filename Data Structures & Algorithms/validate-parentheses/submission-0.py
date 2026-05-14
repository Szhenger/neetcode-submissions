class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an open bracket stack and closed bracket hashmap
        openStack = []
        closedMap = {
            ')' : '(', '}' : '{', ']' : '['
        }
        # Iterate over the characters in the input string
        for c in s:
            # If charcters is a closed brackets
            if c in closedMap:
                if openStack and openStack[-1] == closedMap[c]:
                    openStack.pop()
                else:
                    return False
            # Else the character must be open
            else:
                openStack.append(c)
        # Return True if empty else False
        return not openStack 