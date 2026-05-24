class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Get default pointer for the input array
        index0, index1 = 0, len(numbers) - 1
        # Search for the target in the input array
        while index0 < index1:
            # Compute the number
            number = numbers[index0] + numbers[index1]
            # Update the pointers
            if number < target:
                index0 += 1
            elif number > target:
                index1 -= 1
            # Found the solution
            else:
                return [index0 + 1, index1 + 1]

