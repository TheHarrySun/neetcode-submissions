# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        prev = None
        curr = slow
        while fast:
            prev = curr
            curr = curr.next
            fast = fast.next
        if curr == head:
            return head.next
        prev.next = curr.next
        return head