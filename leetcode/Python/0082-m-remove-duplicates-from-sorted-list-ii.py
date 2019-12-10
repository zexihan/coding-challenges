# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Linked List
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curt = head

        while curt and curt.next:
            if curt.val == curt.next.val:
                dupVal = curt.val
                while curt and curt.val == dupVal:
                    prev.next = curt.next
                    curt = curt.next
            else:
                prev = prev.next
                curt = curt.next
        return dummy.next