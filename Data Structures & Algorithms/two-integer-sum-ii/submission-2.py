class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Get the default pointers of indices
        leftPtr, rightPtr = 0, len(numbers) - 1
        # Two-pointer algorithm 
        while leftPtr < rightPtr:
            # Compute the sum of the referenced values
            curSum = numbers[leftPtr] + numbers[rightPtr]
            # Case 1: curSum == target
            if curSum == target:
                return [leftPtr + 1, rightPtr + 1]
            # Case 2: curSum < target
            elif curSum < target:
                leftPtr += 1
            # Case 3: curSum > target
            else:
                rightPtr -= 1
         