# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        if abs(left - right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else: 
            return False
    
    def height(self, root):
        if not root:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        return max(left, right) + 1 