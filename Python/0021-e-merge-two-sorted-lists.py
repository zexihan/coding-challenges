# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Linked List
Iteration
Time: O(m + n)
Space: O(1)
"""
class Solution_1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0) 
        curt = dummy
        while l1 and l2: 
            if l1.val < l2.val: 
                curt.next = l1
                l1 = l1.next 
            else: 
                curt.next = l2
                l2 = l2.next 
            curt = curt.next
        curt.next = l1 if l1 else l2
        return dummy.next

"""
Recursion
Time: O(m + n)
Space: O(m + n)
"""
class Solution_2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: 
            return l1 or l2 
        if l1.val < l2.val: 
            l1.next = self.mergeTwoLists(l1.next, l2) 
            return l1 
        else: 
            l2.next = self.mergeTwoLists(l1, l2.next) 
            return l2
