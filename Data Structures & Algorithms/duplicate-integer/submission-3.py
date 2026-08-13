class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Get an empty Python set of integers
        seen = set()
        # Iterate over the input Python list of integers
        for num in nums:
            # Short-circuit
            if num in seen:
                return True
            seen.add(num)
        # Has no duplicate
        return False