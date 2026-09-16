class Solution:
    def countSubstrings(self, s: str) -> int:
        # Initialize counter variable to maintain substrings
        count = 0
        # Search for all palindromic substrings
        for i in range(len(s)):
            # Odd length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            # Even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count