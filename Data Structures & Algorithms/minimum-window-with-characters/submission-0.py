class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # Get the window of s and counter of t
        window, counter = defaultdict(int), defaultdict(int)
        for c in t:
            counter[c] += 1
        # Maintain the size of window and counter
        have, need = 0, len(counter)
        minWin, minLen = (-1, -1), float('inf')
        # Sliding window technique
        l = 0
        for r in range(len(s)):
            # Update the window
            window[s[r]] += 1
            if s[r] in counter and window[s[r]] == counter[s[r]]:
                have += 1
            # Have the substring
            while have == need:
                # Update the result
                if r - l + 1 < minLen:
                    minWin, minLen = (l, r), (r - l + 1)
                # Left pop our window
                window[s[l]] -= 1
                if s[l] in counter and window[s[l]] < counter[s[l]]:
                    have -= 1
                l += 1
        l, r = minWin
        return s[l:r+1] if minLen < float('inf') else ""

