# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_sequence(root):
            result = []

            def dfs(root):
                if not root:
                    return

                if not root.left and not root.right:
                    result.append(root.val)
                    return

                if root.left:
                    dfs(root.left)

                if root.right:
                    dfs(root.right)

            dfs(root)

            return result

        return get_leaf_sequence(root1) == get_leaf_sequence(root2)