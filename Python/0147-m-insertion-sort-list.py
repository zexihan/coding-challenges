# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head
        dummy = ListNode(0)
        dummy.next = head
        while head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                temp = head.next
                q = dummy
                head.next = head.next.next
                while q.next and q.next.val < temp.val:
                    q = q.next
                temp.next = q.next
                q.next = temp
        return dummy.next
