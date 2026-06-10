class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Get a length variable and default dictionary of letters in s
        maxLen, count = 0, defaultdict(int)
        # Sliding window algorithm
        left = 0
        for right in range(len(s)):
            # Extend the window
            count[s[right]] += 1
            # Push the window if replacement fails
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            # Find the local max length
            maxLen = max(maxLen, right - left + 1)
        # Return the global max length
        return maxLen 

