class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])

        def get_adj_cells(r, c):
            result = []

            directions = (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
                (1, -1),
                (1, 1),
                (-1, 1),
                (-1, -1),
            )

            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n:
                    result.append((r + dr, c + dc)) 

            return result

        def reveal(r, c, initial=False):
            if board[r][c] == 'M':
                if initial:
                    board[r][c] = 'X'
                return

            if board[r][c] != 'E':
                return

            adj_mines = 0
            adj_cells = get_adj_cells(r, c)

            for ar, ac in adj_cells:
                if board[ar][ac] == 'M':
                    adj_mines += 1

            if adj_mines == 0:
                board[r][c] = 'B'
                for ar, ac in adj_cells:
                    reveal(ar, ac)
            else:
                board[r][c] = str(adj_mines)

        reveal(click[0], click[1], initial=True)
        return board