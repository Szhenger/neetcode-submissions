class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # Initalize an order list of integers
        spiral = []
        # Four-pointer algorithm
        top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
        while top < bottom and left < right:
            # Top row
            for i in range(left, right):
                spiral.append(matrix[top][i])
            top += 1
            # Right column
            for i in range(top, bottom):
                spiral.append(matrix[i][right - 1])
            right -= 1
            # Edge case
            if top == bottom or left == right:
                break
            # Bottom row
            for i in range(right - 1, left - 1, -1):
                spiral.append(matrix[bottom - 1][i])
            bottom -= 1
            # Left column
            for i in range(bottom - 1, top - 1, -1):
                spiral.append(matrix[i][left])
            left += 1
        return spiral
