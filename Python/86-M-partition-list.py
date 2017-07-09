# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Time:
# Space:
class Solution_1(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p = head
        shead = ListNode(0)
        lhead = ListNode(0)
        s = shead
        l = lhead

        while p:
            if p.val < x:
                s.next = p
                p = p.next
                s = s.next
                s.next = None
            else:
                l.next = p
                p = p.next
                l = l.next
                l.next = None

        s.next = lhead.next
        head = shead.next
        return head

# Time:
# Space:
class Solution_2(object):
    # in-place solution
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smallPre = ListNode(0)
        largePre = ListNode(0)
        smallDummy = smallPre
        largeDummy = largePre

        while head:

            if head.val < x:
                smallPre.next = head
                smallPre = smallPre.next
            else:
                largePre.next = head
                largePre = largePre.next

            head = head.next

        largePre.next = None
        smallPre.next = largeDummy.next
        head = smallDummy.next

        return head