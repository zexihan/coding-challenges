"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution_1(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        if root.left and root.right:
            root.left.next = root.right
            tmp = root.next
            while tmp:
                if tmp.left:
                    root.right.next = tmp.left
                    break
                if tmp.right:
                    root.right.next = tmp.right
                    break
                tmp = tmp.next
        elif root.left:
            tmp = root.next
            while tmp:
                if tmp.left:
                    root.left.next = tmp.left
                    break
                if tmp.right:
                    root.left.next = tmp.right
                    break
                tmp = tmp.next
        elif root.right:
            tmp = root.next
            while tmp:
                if tmp.left:
                    root.right.next = tmp.left
                    break
                if tmp.right:
                    root.right.next = tmp.right
                    break
                tmp = tmp.next
        self.connect(root.right)
        self.connect(root.left)
        # @connect(root.right)should be the first!!!
        return root


class Solution_2(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        p = root
        q = None
        nextNode = None
        while p:
            if p.left:
                if q:
                    q.next = p.left
                q = p.left
                if nextNode == None:
                    nextNode = q
            if p.right:
                if q: 
                    q.next = p.right
                q = p.right
                if nextNode == None:
                    nextNode = q
            p = p.next
        self.connect(nextNode)
        return root

        
