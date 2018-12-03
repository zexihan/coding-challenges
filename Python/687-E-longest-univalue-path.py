# Tree, Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return max(self.longestLength(root.left, root.val) + self.longestLength(root.right, root.val),
                   self.longestUnivaluePath(root.left),
                   self.longestUnivaluePath(root.right))
    
    def longestLength(self, root, val):
        if not root or root.val != val:
            return 0
        return 1 + max(self.longestLength(root.left, val), self.longestLength(root.right, val))