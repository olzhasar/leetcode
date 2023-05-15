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
        def helper(r, c, n) -> 'Node':
            node = Node(grid[r][c] == 1, True, None, None, None, None)
            if n <= 1:
                return node
            
            all_same = True
            values = {grid[r][c]}
            
            for xr in range(r, r + n):
                for xc in range(c, c + n):
                    if grid[xr][xc] not in values:
                        all_same = False
                        break
                if not all_same:
                    break
                       
            if all_same:
                return node
            
            n = n // 2
            
            node.isLeaf = False
            node.topLeft = helper(r, c, n)
            node.topRight = helper(r, c + n, n)
            node.bottomLeft = helper(r + n, c, n)
            node.bottomRight = helper(r + n, c + n, n)
            
            return node
        
        return helper(0, 0, len(grid))