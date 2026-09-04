class Solution:
    def partition(self, s: str) -> List[List[str]]:
        strs = []
        def backtrack(i: int) -> None:
            if i >= len(s):
                strs.append(part[:])
            else:
                for j in range(i, len(s)):
                    if isPal(s, i, j):
                        part.append(s[i : j + 1])
                        backtrack(j + 1)
                        part.pop()
        part = []
        def isPal(s: str, l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        backtrack(0)
        return strs