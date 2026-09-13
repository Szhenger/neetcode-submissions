class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top, bottom = 0, len(matrix) - 1
        while top < bottom:
            for index in range(bottom - top):
                left, right = top, bottom
                topLeft = matrix[top][left + index]
                matrix[top][left + index] = matrix[bottom - index][left]
                matrix[bottom - index][left] = matrix[bottom][right - index]
                matrix[bottom][right - index] = matrix[top + index][right]
                matrix[top + index][right] = topLeft
            top += 1
            bottom -= 1
