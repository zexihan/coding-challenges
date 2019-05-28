# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        root = self.helper(head, None)
        return root
        
    def helper(self, head, tail):
        if head == tail:
            return None
        slow = head
        fast = head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        node = TreeNode(slow.val)
        node.left = self.helper(head, slow)  
        node.right = self.helper(slow.next, tail)
        return node

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)

run = Solution()
print(run.sortedListToBST(head).val)