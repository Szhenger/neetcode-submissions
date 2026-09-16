class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int: 
        # Count the fresh fruit and enqueue the rotten fruit
        fresh, queue = 0, deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        # Breadth-first search the grid of fresh or rotten fruit
        time, direction = 0, ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and 
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            time += 1
        return time if not fresh else -1
            