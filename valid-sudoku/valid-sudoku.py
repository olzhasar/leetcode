class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False

                box_num = (i // 3) * 3 + (j // 3)
                if num in boxes[box_num]:
                    return False
                    
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_num].add(num)

        return True