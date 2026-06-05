class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Get a default length variable and empty hashset of characters
        maxLen, windowSet, windowAdr = 0, set(), 0
        # Iterate over the string of characters
        for c in s:
            while c in windowSet:
                windowSet.remove(s[windowAdr])
                windowAdr += 1
            windowSet.add(c)
            maxLen = max(maxLen, len(windowSet))
        # Return the max substring length 
        return maxLen