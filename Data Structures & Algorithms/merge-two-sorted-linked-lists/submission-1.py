# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            A, B = list1, list2
        else:
            A, B = list2, list1
        
        prev = A
        curr_A = A.next
        curr_B = B
        while curr_A and curr_B:
            if curr_A.val <= curr_B.val:
                prev.next = curr_A
                prev = prev.next
                curr_A = curr_A.next
            else:
                prev.next = curr_B
                prev = prev.next
                curr_B = curr_B.next
        if not curr_A:
            prev.next = curr_B
        elif not curr_B:
            prev.next = curr_A
        return A