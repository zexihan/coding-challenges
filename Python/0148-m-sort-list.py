# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        slow = head
        fast = head.next.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        p2 = self.sortList(slow.next)
        slow.next = None
        p1 = self.sortList(head)
        return self.merge(p1,p2)
    
    def merge(self, p1, p2):
        p, dummy = ListNode(0), ListNode(0)
        p = dummy
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1 == None:
            p.next = p2
        else:
            p.next = p1
        return dummy.next
        