class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen, winSet, winIdx = 0, set(), 0
        for c in s:
            while c in winSet:
                winSet.remove(s[winIdx])
                winIdx += 1
            winSet.add(c)
            maxLen = max(maxLen, len(winSet))
        return maxLen
            


        