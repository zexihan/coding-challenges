# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            pre.next = cur.next
            cur.next = pre.next.next # or cur.next.next
            pre.next.next = cur
            pre = cur
            cur = cur.next
        return dummy.next
            


