# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        answer = []
        
        i = 0
        
        while head:
            while stack and head.val > stack[-1][0]:
                prev_val, prev_idx = stack.pop()
                answer[prev_idx] = head.val
            stack.append((head.val, i))
            answer.append(0)
            
            head = head.next
            i += 1
            
        return answer