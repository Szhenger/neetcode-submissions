class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Get default pointers for the input string
        i, j = 0, len(s) - 1
        # Validate if the input string is a palindrome
        while i < j:
            # Skip the non-alphanumeric characters
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            # Match the characters in the input string
            if s[i].lower() != s[j].lower():
                return False
            # Update the pointers 
            i += 1
            j -= 1
        return True