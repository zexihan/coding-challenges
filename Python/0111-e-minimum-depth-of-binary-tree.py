# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and root.right:
            return self.minDepth(root.right) + 1
        if root.left and not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

class Solution_2:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.getMin(root)
    
    def getMin(self, node):
        if not node:
            return float('inf')

        if not node.left and not node.right:
            return 1
        
        left = self.getMin(node.left)
        right = self.getMin(node.right)

        return min(left, right) + 1