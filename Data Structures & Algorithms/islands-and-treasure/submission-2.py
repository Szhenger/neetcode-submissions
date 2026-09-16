class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        # Enqueue the treasure coordinates
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
        INF = 2 ** 31 - 1
        # Breadth-first search algorithm
        delta = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            r, c = queue.popleft()
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and
                    grid[nr][nc] == INF):
                    grid[nr][nc] = 1 + grid[r][c]
                    queue.append((nr, nc)) 
             

        