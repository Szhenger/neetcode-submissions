class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        ROWS = COLS = len(matrix)
        # Reverse the columns
        for col in range(COLS):
            i, j = 0, ROWS - 1
            while i < j:
                matrix[i][col], matrix[j][col] = matrix[j][col], matrix[i][col]
                i += 1
                j -= 1
        # Transpose the matrix
        for row in range(ROWS):
            for col in range(row, COLS):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        return None
