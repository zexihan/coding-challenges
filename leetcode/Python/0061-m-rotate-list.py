# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Linked List
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        curt = head
        size = 0
        while curt:
            size += 1
            curt = curt.next
        
        k = k % size
        if k == 0:
            return head
        
        slow = fast = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        newHead = slow.next
        fast.next = head
        slow.next = None
        return newHead