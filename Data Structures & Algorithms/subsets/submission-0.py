class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        def dfs(idx: int, sub: List[int]) -> None:
            if idx == len(nums):
                sets.append(sub)
            elif idx < len(nums):
                dfs(idx + 1, sub)
                dfs(idx + 1, sub + [nums[idx]])
        dfs(0, [])
        return sets

                
