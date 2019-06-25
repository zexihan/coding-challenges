# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root or L > R:
            return None
        self.sum = 0
        self.inorder(root, L, R)
        return self.sum
    
    def inorder(self, node, L, R):
        if not node:
            return
        if L <= node.val <= R:
            self.sum += node.val
        if L < node.val:
            self.inorder(node.left, L, R)
        if node.val < R:
            self.inorder(node.right, L, R)