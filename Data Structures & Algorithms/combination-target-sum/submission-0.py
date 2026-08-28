class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        def dfs(index: int, combo: List[int], total: int) -> None:
            if total == target:
                combos.append(combo)
            elif index < len(nums) and total < target:
                dfs(index, combo + [nums[index]], total + nums[index])
                dfs(index + 1, combo, total)
        dfs(0, [], 0)
        return combos