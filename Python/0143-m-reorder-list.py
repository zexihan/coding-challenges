# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # step 1: find the mid point
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # step 2: reverse the second half in-place
        p = slow
        q = slow.next
        slow.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        pre = p
        #pre, node = None, slow
        #while node:
        #    pre, node.next, node = node, pre, node.next
        
        # step 3: merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        
        return head

if __name__ == "__main__":
    x = ListNode(1)
    x.next = ListNode(2)
    x.next.next = ListNode(3)
    x.next.next.next = ListNode(4)
    x.next.next.next.next = ListNode(5)
    x.next.next.next.next.next = ListNode(6)
    new = Solution()
    print(new.reorderList(x).next.next.next.next.val)