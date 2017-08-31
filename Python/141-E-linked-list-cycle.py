# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        walker = head
        runner = head
        while runner.next is not None and runner.next.next is not None:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False