class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # Get the dimensions of heights matrix
        ROWS, COLS = len(heights), len(heights[0])
        # Depth-first search from the oceans
        def dfs(row: int, col: int, visit: set[tuple[int]], preHeight: int) -> None:
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                (row, col) in visit or
                heights[row][col] < preHeight):
                return None
            visit.add((row, col))
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])
        # Initialize the visit sets of coordinates
        pacific, atlantic = set(), set()
        # DFS by the left and right columns
        for row in range(ROWS):
            dfs(row, 0, pacific, float('-inf'))
            dfs(row, COLS - 1, atlantic, float('-inf'))
        # DFS by the top and bottom rows
        for col in range(COLS):
            dfs(0, col, pacific, float('-inf'))
            dfs(ROWS - 1, col, atlantic, float('-inf'))
        # Intersect the pacific and atlantic coordinates
        intersection = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    intersection.append([row, col])
        return intersection

            
            


        