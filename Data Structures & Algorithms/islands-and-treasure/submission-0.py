class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        # Enqueue the treasure coordinates
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append([i, j, grid[i][j]])
        # Breadth-first search algorithm
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c, d = queue.popleft()
            for ir, jc in delta:
                nr, nc = r + ir, c + jc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > d + 1:
                    grid[nr][nc] = d + 1
                    queue.append([nr, nc, grid[nr][nc]]) 
             

        