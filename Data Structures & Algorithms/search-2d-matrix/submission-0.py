class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the dimensions of the matrix list
        m, n = len(matrix), len(matrix[0])
        # Binary search for the correct row
        row, left, right = -1, 0, m - 1
        while left <= right:
            row = (left + right) // 2
            if matrix[row][0] > target:
                right = row - 1
            elif matrix[row][n - 1] < target:
                left = row + 1
            else:
                break
        # Binary search for the correct column
        col, left, right = -1, 0, n - 1
        while left <= right:
            col = (left + right) // 2
            if matrix[row][col] < target:
                left = col + 1
            elif matrix[row][col] > target:
                right = col - 1
            else:
                return True
        # Binary search FAILED
        return False




