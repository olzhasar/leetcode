from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 0
        max_sum = float("-inf")
        current_level = 1

        while queue:
            current_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()

                if not node:
                    continue

                current_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if current_sum > max_sum:
                max_sum = current_sum
                level = current_level
            
            current_level += 1

        return level