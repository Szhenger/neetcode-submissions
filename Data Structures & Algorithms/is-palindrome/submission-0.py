class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initilize a two-pointer approach 
        l, r = 0, len(s) - 1
        while l < r:
            # Skip non-alphnumeric characters
            while l < r and not s[l].isalnum(): 
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # Compute if not match 
            if s[l].lower() != s[r].lower():
                return False
            # Increment and decrement the left and right pointers
            l += 1
            r -= 1
        # Input string must be valid
        return True