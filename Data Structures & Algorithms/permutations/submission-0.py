class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def dfs(perm: List[int], candidates: List[int]):
            if not candidates:
                perms.append(perm)
            for i, candidate in enumerate(candidates):
                dfs(perm + [candidates[i]], candidates[:i] + candidates[i + 1:])
        dfs([], nums)
        return perms