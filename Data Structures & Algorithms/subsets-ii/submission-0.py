class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powSet = []
        def backtrack(idx: int, subSet: List[int]) -> None:
            if idx >= len(nums):
                powSet.append(subSet.copy())
            else:
                subSet.append(nums[idx])
                backtrack(idx + 1, subSet)
                subSet.pop()
                while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                    idx += 1
                backtrack(idx + 1, subSet)
        nums.sort()
        backtrack(0, [])
        return powSet