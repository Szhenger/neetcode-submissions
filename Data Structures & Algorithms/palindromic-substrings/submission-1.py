class Solution:
    def countSubstrings(self, s: str) -> int:
        # Initialize counter variable to maintain substrings
        state = 0
        # Count all palindromic substrings
        def countPalindromes(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        for i in range(len(s)):
            # Odd length
            state += countPalindromes(i, i)
            # Even length
            state += countPalindromes(i, i + 1)
        return state