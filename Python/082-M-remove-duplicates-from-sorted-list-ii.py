# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = dummy.next

        while cur:
            while cur.next and cur.next.val == pre.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next