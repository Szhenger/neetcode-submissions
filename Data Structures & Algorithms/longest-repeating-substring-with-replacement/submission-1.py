class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen, cntLet = 0, defaultdict(int)
        # Sliding window technique
        lef = 0
        for rig in range(len(s)):
            cntLet[s[rig]] += 1
            while (rig - lef + 1) - max(cntLet.values()) > k:
                cntLet[s[lef]] -= 1
                lef += 1
            maxLen = max(maxLen, rig - lef + 1)
        return maxLen