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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = ListNode(0)
        dummy.next = cur
        carry = 0
        while True:
            if l1:
                cur.val += l1.val
                l1 = l1.next
            if l2:
                cur.val += l2.val
                l2 = l2.next
            
            cur.val += carry
            if cur.val >= 10:
                cur.val %= 10
                carry = 1
            else:
                carry = 0
            
            if l1 or l2 or carry:
                cur.next = ListNode(0)
                cur = cur.next
            else:
                break

        return dummy.next