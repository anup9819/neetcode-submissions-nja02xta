# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_blank, current = None, head

        while current:
            next_elem = current.next
            current.next = previous_blank
            previous_blank = current
            current = next_elem
        return previous_blank
        