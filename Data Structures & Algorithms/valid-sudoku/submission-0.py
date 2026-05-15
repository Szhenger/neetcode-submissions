class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Get default hashmaps of empty hashsets
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        # Validate the Rules
        for r in range(len(board)):
            for c in range(len(board[0])):
                # Continue if not digit
                if board[r][c] == '.':
                    continue
                # Compute if digit seen
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[(r // 3, c // 3)]):
                    return False
                # Add the digit to the hashmaps
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        return True
                


                

        