# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        A, B = l1, l2
        res = ListNode(-1)
        res_head = res
        remainder = 0
        while A or B or remainder != 0:
            if A and B:
                digit = A.val + B.val + remainder
                A = A.next
                B = B.next
            elif A:
                digit = A.val + remainder
                A = A.next
            elif B:
                digit = B.val + remainder
                B = B.next
            else:
                digit = remainder
            res.next = ListNode(digit % 10)
            res = res.next
            remainder = digit // 10
        return res_head.next