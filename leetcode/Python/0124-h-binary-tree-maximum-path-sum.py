# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Recursion - Divide and Conquer
Time: O(n)
Space: O(logn)
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        _, any2any = self.helper(root)
        return any2any
    
    def helper(self, root):
        if not root:
            return float('-inf'), float('-inf')
        
        # divide
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        # conquer
        root2any = max(max(left[0], right[0]), 0) + root.val
        
        any2any = max(left[1], right[1])
        
        any2any = max(any2any, max(left[0], 0) + root.val + max(right[0], 0))
        
        return root2any, any2any