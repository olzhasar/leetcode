# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        if not head:
            return head

        even_root = head.next
        even = head.next

        while even and even.next:
            odd.next = even.next
            even.next = odd.next.next

            odd = odd.next
            even = even.next

        odd.next = even_root

        return head