# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Linked List
1. find the m-1th node
2. reverse m to n
3. connect
"""
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m >= n:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        node = dummy
        # find the m-1th node
        for i in range(1, m):
            if not node:
                return None
            node = node.next
        
        if not node.next:
            return None
        
        # reverse
        premNode = node
        mNode = node.next
        nNode = mNode
        postnNode = mNode.next
        for i in range(m, n):
            if not postnNode:
                return None
            temp = postnNode.next
            postnNode.next = nNode
            nNode = postnNode
            postnNode = temp
        
        # connect
        mNode.next = postnNode
        premNode.next = nNode
        return dummy.next