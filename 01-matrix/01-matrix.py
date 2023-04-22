class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        output = [[math.inf for _ in range(n)] for _ in range(m)]

        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
        
        def get_adj_cells(row, col):
            directions = (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            )
            for drow, dcol in directions:
                if 0 <= row + drow < m and 0 <= col + dcol < n:
                    yield row + drow, col + dcol
            
        def append_adj(row, col):
            for x, y in get_adj_cells(row, col):
                queue.append((x, y))
        
        dist = 0

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if output[x][y] > dist:
                    output[x][y] = dist
                    append_adj(x, y)
            dist += 1
                
        return output