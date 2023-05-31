class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = set()
        
        directions = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        )
        
        def get_paths(i, j):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < m) and (0 <= nj < n) and grid[ni][nj] != 0 and (ni, nj) not in visited:
                    yield ni, nj
        
        def dfs(i, j):
            visited.add((i, j))
            
            max_path = 0
            for ni, nj in get_paths(i, j):
                max_path = max(max_path, dfs(ni, nj))
            
            visited.remove((i, j))
            
            return grid[i][j] + max_path
        
        max_gold = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j))
                
        return max_gold