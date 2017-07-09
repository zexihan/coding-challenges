# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time:
# Space:
class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = fast = dummy
        # move fast pointer n steps
        for i in range(n):
            fast = fast.next
        # move together till end
        while fast.next:
            fast = fast.next
            slow = slow.next
        # remove nth
        slow.next = slow.next.next

        return dummy.next
