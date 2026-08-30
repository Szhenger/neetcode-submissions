class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(row: int, col: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if (row < 0 or col < 0 or 
                row >= ROWS or col >= COLS or 
                board[row][col] != word[idx] or (row, col) in path):
                return False
            path.add((row, col))
            res = (dfs(row + 1, col, idx + 1) or
                   dfs(row - 1, col, idx + 1) or
                   dfs(row, col + 1, idx + 1) or
                   dfs(row, col - 1, idx + 1))
            path.remove((row, col))
            return res
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0): return True
        return False
            

