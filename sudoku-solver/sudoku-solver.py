class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        _get_box_num = lambda r, c:  r // 3 * 3 + c // 3

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[_get_box_num(r, c)].add(board[r][c])

        def backtrack() -> bool:
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        box_num = _get_box_num(r, c)
                        for k in range(1, 10):
                            val = str(k)
                            if val in rows[r] or val in cols[c] or val in boxes[box_num]:
                                continue
                            board[r][c] = val
                            rows[r].add(val)
                            cols[c].add(val)
                            boxes[box_num].add(val)
                            if backtrack():
                                return True
                            board[r][c] = "."
                            rows[r].discard(val)
                            cols[c].discard(val)
                            boxes[box_num].discard(val)
                        return False

            return True

        backtrack()