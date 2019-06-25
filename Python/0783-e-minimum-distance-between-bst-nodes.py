# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.prev = float('-inf')
        self.res = float('inf')
        self.inorder(root)
        return self.res
    
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.res = min(self.res, node.val - self.prev)
        self.prev = node.val
        self.inorder(node.right)