import functools


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longest = 0
        m = len(matrix)
        n = len(matrix[0])

        @functools.cache
        def dfs(r, c):
            directions = (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
            )

            max_result = 0

            for dr, dc in directions:
                if 0 <= dr + r < m and 0 <= dc + c < n and matrix[dr + r][dc + c] > matrix[r][c]:
                    max_result = max(max_result, dfs(dr + r, dc + c))

            return max_result + 1

        for r in range(m):
            for c in range(n):
                longest = max(longest, dfs(r, c))

        return longest