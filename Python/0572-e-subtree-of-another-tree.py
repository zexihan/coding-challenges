# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        return self.equals(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def equals(self, x, y):
        if not x and not y:
            return True
        if not x or not y:
            return False
        return x.val == y.val and self.equals(x.left, y.left) and self.equals(x.right, y.right)