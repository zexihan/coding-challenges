# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
recursive
Time: O(h) 
balanced - O(logn), unbalanced - O(n)
"""
class Solution_1:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root or not p:
            return None
        if root.val <= p.val: 
            return self.inorderSuccessor(root.right, p)
        else:
            return self.inorderSuccessor(root.left, p) or root

"""
iterative
"""
class Solution_2:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None or p is None:
            return None
        
        successor = None
        while root is not None:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        
        return successor

