class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]

        _get_box_num = lambda r, c:  r // 3 * 3 + c // 3

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = int(board[r][c]) - 1
                    rows[r][val] = 1
                    cols[c][val] = 1
                    boxes[_get_box_num(r, c)][val] = 1

        def backtrack() -> bool:
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        box_num = _get_box_num(r, c)
                        for k in range(9):
                            if rows[r][k] or cols[c][k] or boxes[box_num][k]:
                                continue
                            board[r][c] = str(k + 1)
                            rows[r][k] = 1
                            cols[c][k] = 1
                            boxes[box_num][k] = 1
                            if backtrack():
                                return True
                            board[r][c] = "."
                            rows[r][k] = 0
                            cols[c][k] = 0
                            boxes[box_num][k] = 0
                        return False

            return True

        backtrack()