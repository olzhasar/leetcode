# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = None
        node = root

        while node and node.val != key:
            parent = node
            if key > node.val:
                node = node.right
            else:
                node = node.left

        if not node:
            return root

        if node.left and node.right:
            smallest = node.right
            while smallest and smallest.left:
                smallest = smallest.left
            smallest.left = node.left
            node = node.right
        elif node.left:
            node = node.left
        else:
            node = node.right
        
        if not parent:
            return node
        
        if key > parent.val:
            parent.right = node
        else:
            parent.left = node

        return root