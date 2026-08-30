class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        def dfs(index: int, combo: List[int], total: int):
            if total == target:
                combos.append(combo)
            elif total < target and index < len(candidates):
                dfs(index + 1, combo + [candidates[index]], total + candidates[index])
                while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                    index += 1
                dfs(index + 1, combo, total)
        candidates.sort()
        dfs(0, [], 0)
        return combos
