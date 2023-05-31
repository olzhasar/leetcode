class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check_num(r, c, k):
            # check row and column
            for i in range(9):
                if board[i][c] == k or board[r][i] == k:
                    return False

            # check square
            min_row = r - r % 3
            max_row = min_row + 3

            min_col = c - c % 3
            max_col = min_col + 3

            for i in range(min_row, max_row):
                for j in range(min_col, max_col):
                    if board[i][j] == k:
                        return False

            return True

        def backtrack() -> bool:
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for k in range(1, 10):
                            if not check_num(r, c, str(k)):
                                continue
                            board[r][c] = str(k)
                            if backtrack():
                                return True
                            board[r][c] = "."
                        return False

            return True

        backtrack()