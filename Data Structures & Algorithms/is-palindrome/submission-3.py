class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two-pointer algorithm
        left, right = 0, len(s) - 1
        while left < right:
            # Skip non-alphanumeric chars
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            # Verify alphanumeric chars
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True 

