class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, top, bot = None, 0, len(matrix) - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][0] <= target <= matrix[row][len(matrix[0]) - 1]:
                break
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                top = row + 1
        col, lef, rig = None, 0, len(matrix[0]) - 1
        while lef <= rig:
            col = (lef + rig) // 2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                rig = col - 1
            else:
                lef = col + 1
        return False
