# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Linked List
1. find the mid point
2. reverse the second half
3. merge
"""
class Solution:
    def _splitList(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        return head, middle

    def _reverseList(self, head):
        prev = None
        curt = head
        while curt:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
        return prev

    def _mergeList(self, head1, head2):
        while head2:
           temp = head2.next
           head2.next = head1.next
           head1.next = head2
           head1 = head1.next.next
           head2 = temp

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # find the mid point
        head1, head2 = self._splitList(head)

        # reverse the second half
        head2 = self._reverseList(head2)

        #  merge
        self._mergeList(head1, head2)
