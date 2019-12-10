# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Linked List
Iterative
"""
class Solution_1:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curt = head

        while curt:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp

        return prev

"""
Recursive
"""
class Solution_2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
