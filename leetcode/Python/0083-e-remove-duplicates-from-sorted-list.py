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
        curt = head
        while curt and curt.next:
            if curt.next.val == curt.val:
                curt.next = curt.next.next
            else:
                curt = curt.next
        return head
