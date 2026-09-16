class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize the state variables
        i = j = c = 0
        # Determine the longest palindromic substring
        for k in range(len(s)):
            # Odd length
            l = r = k
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > c:
                    i, j = l, r + 1
                    c = r - l + 1
                l -= 1
                r += 1
            # Even length
            l, r = k, k + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > c:
                    i, j = l, r + 1
                    c = r - l + 1
                l -= 1
                r += 1
        return s[i:j]
