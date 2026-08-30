class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def dfs(perm: List[int], cans: List[int]):
            if len(perm) == len(nums):
                perms.append(perm)
            for num in cans:
                dfs(perm + [num], [
                    elem for elem in cans if elem != num
                ])
        dfs([], nums)
        return perms