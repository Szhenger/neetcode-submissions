class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # Two-pointer algorithm
        top, bottom = 0, len(matrix) - 1
        while top < bottom:
            left, right = top, bottom
            # Reverse border in counter-clockwise order
            for index in range(right - left):
                # Save the top left element
                topLeft = matrix[top][left + index]
                # Move the bottom left element
                matrix[top][left + index] = matrix[bottom - index][left]
                # Move the bottom right element
                matrix[bottom - index][left] = matrix[bottom][right - index]
                # Move the top right element
                matrix[bottom][right - index] = matrix[top + index][right]
                # Move the top left element
                matrix[top + index][right] = topLeft
            top += 1
            bottom -= 1
        return None