import functools
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        @functools.lru_cache
        def dfs(node: Optional[TreeNode], prev=0):
            # prev: -1 left, +1 right, 0 - no prev

            if not node:
                return -1

            if not node.right and not node.left:
                return 0

            if prev == 1:
                return dfs(node.left, -1) + 1

            if prev == -1:
                return dfs(node.right, 1) + 1

            return max(dfs(node.left, -1) + 1, dfs(node.right, 1) + 1, dfs(node.left), dfs(node.right))

        return dfs(root)