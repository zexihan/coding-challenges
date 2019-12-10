# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Linked List
"""
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None

        leftDummy = ListNode(0)
        rightDummy = ListNode(0)

        left = leftDummy
        right = rightDummy

        while head:
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head
            head = head.next

        right.next = None
        left.next = rightDummy.next
        return leftDummy.next
