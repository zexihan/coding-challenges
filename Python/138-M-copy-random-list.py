"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
"""
two pass
Time: O(n)
Space: O(n)
"""
class Solution_1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        myMap = {}
        nHead = Node(head.val, None, None)
        myMap[head] = nHead
        p, q = head, nHead
        while p:
            q.random = p.random
            if p.next:
                q.next = Node(p.next.val, None, None)
                myMap[p.next] = q.next
            p = p.next
            q = q.next

        p = nHead
        while p:
            if p.random:
                p.random = myMap[p.random]
            p = p.next
        return nHead


"""
recursive
Time: O(n)
Space: O(n)
"""
class Solution_2:
    def __init__(self):
        self.visitedHash = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        node = Node(head.val, None, None)
        self.visitedHash[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
