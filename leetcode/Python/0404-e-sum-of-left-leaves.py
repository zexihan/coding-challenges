# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Recursion
For given node we check whether its left child is a leaf. If it is the case, 
we add its value to answer, otherwise recursively call method on left child. 
For right child we call method only if it has at least one nonnull child.
"""
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        if root.left:
            if not root.left.left and not root.left.right:
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)

        return res