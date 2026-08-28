class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        c1, c2 = Counter(s1), Counter("")
        l = 0
        for r in range(len(s2)):
            if s2[r] in c1:
                c2[s2[r]] += 1
                while l <= r and c1[s2[r]] < c2[s2[r]]:
                    c2[s2[l]] -= 1
                    l += 1
            else:
                while l <= r:
                    if s2[l] in c2:
                        c2[s2[l]] -= 1
                    l += 1
            if c1 == c2:
                return True
        return False 