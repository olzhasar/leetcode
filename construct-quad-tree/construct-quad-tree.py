"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def all_same(r, c, n):
            for xr in range(r, r + n):
                for xc in range(c, c + n):
                    if grid[xr][xc] != grid[r][c]:
                        return False
            return True

        def helper(r, c, n) -> 'Node':
            node = Node(grid[r][c] == 1, True, None, None, None, None)
            if n <= 1 or all_same(r, c, n):
                return node
            
            n = n // 2
            
            node.isLeaf = False
            node.topLeft = helper(r, c, n)
            node.topRight = helper(r, c + n, n)
            node.bottomLeft = helper(r + n, c, n)
            node.bottomRight = helper(r + n, c + n, n)
            
            return node
        
        return helper(0, 0, len(grid))