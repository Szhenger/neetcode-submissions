class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powSet = []
        def dfs(index: int, subset: List[int]) -> None:
            if index >= len(nums):
                powSet.append(subset)
            else:
                dfs(index + 1, subset)
                dfs(index + 1, subset + [nums[index]])
        dfs(0, [])
        return powSet

                
