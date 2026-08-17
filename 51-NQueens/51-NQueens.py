# Last updated: 8/16/2026, 9:53:12 PM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # DFS backtracking of every row
        # Collision: same row, same col, (left diagonal: same "r+c"), (right diagonal: same "r-c")
        result = []
        cols = set()    # occupied cols
        diag1 = set()   # occupied left diagonal
        diag2 = set()   # occupied right diagonal
        board = [["."] * n for _ in range(n)]   # current board

        def backtrack(row: int):
            # exit
            if row == n:
                # already searching all [0, n-1] rows
                result.append(["".join(r) for r in board])
                return
            
            # iterate cols under the curr "row"
            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue
                
                # add current node into board
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                # backtracking all possibilites based on the current node
                # since no same row rule, searching from 'row+1'
                backtrack(row + 1)

                # cancel the current node
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
        
        backtrack(0)
        return result

