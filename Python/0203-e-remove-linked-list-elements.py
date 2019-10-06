# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        p = head
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else: 
                p = p.next
        return head