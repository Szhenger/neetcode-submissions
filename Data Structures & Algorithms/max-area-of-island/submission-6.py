class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(i: int, j: int) -> int:
            if (i < 0 or j < 0 or
                i == ROWS or j == COLS or
                grid[i][j] == 0):
                return 0
            grid[i][j] = 0
            return (1 + dfs(i + 1, j) + 
                        dfs(i - 1, j) + 
                        dfs(i, j + 1) + dfs(i, j - 1))
        maxArea = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))
        return maxArea