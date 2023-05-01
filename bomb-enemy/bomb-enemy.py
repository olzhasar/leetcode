class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row_kills = 0
        max_kills = 0
        col_kills = [0] * n
        
        for r in range(m):
            for c in range(n):
                if c == 0 or grid[r][c - 1] == 'W':
                    row_kills = 0
                    for k in range(c, n):
                        if grid[r][k] == 'W':
                            break
                        elif grid[r][k] == 'E':
                            row_kills += 1

                if r == 0 or grid[r - 1][c] == 'W':
                    col_kills[c] = 0
                    for k in range(r, m):
                        if grid[k][c] == 'W':
                            break
                        elif grid[k][c] == 'E':
                            col_kills[c] += 1

                if grid[r][c] == '0':
                    current_kills = row_kills + col_kills[c]
                    max_kills = max(current_kills, max_kills)
                    
        return max_kills