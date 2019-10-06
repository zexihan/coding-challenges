# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Recursion
Time: O(n)
Space: O(logn)
"""
class Solution_1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
            self.isSameTree(p.left, q.left)

"""
Recursion
Time: O(n)
Space: O(logn)
"""
from collections import deque
class Solution_2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            # if both are none
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
        
        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        
        return True