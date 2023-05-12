from copy import deepcopy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0] * n for _ in range(n)]

        result = []

        def save_result(board):
            output = []

            for row in board:
                row_str = ""
                for val in row:
                    if val == 1:
                        row_str += "Q"
                    else:
                        row_str += "."
                output.append(row_str)

            result.append(output)

        def place_queen(board, ir, ic):
            changed = [(ir, ic)]
            board[ir][ic] = 1

            directions = (
                (-1, -1),
                (1, -1),
                (1, 1),
                (-1, 1),
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
            )

            for dr, dc in directions:
                r, c = ir + dr, ic + dc
                while 0 <= r < n and 0 <= c < n:
                    if board[r][c] == 0:
                        changed.append((r, c))
                        board[r][c] = 2
                    r += dr
                    c += dc
            
            return changed

        def backtrack(board, start=0, q=0):
            if q == n:
                save_result(board)
                return

            for i in range(start, n * n):
                r = i // n
                c = i % n

                if board[r][c] != 0:
                    continue

                changed = place_queen(board, r, c)
                backtrack(board, i + 1, q + 1)
                for cr, cc in changed:
                    board[cr][cc] = 0

        backtrack(board)

        return result