class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def get_adj_cells(i, j):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for di, dj in directions:
                if 0 <= i + di < rows and 0 <= j + dj < cols and not visited[i + di][j + dj]:
                    yield i + di, j + dj

        def backtrack(i, j, suffix):
            if not suffix:
                return True

            visited[i][j] = True

            for ai, aj in get_adj_cells(i, j):
                if board[ai][aj] != suffix[0]:
                    continue
                if backtrack(ai, aj, suffix[1:]):
                    return True

            visited[i][j] = False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(i, j, word[1:]):
                        return True

        return False