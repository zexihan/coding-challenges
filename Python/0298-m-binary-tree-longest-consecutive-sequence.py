# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Recursion - Divide and Conquer
Time: O(n)
Space: O(n)
"""
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root: 
            return 0
        
        left = self.helper(root.left) + 1
        right = self.helper(root.right) + 1
        
        if root.left and root.val != root.left.val - 1:
            left = 1
        
        if root.right and root.val != root.right.val - 1:
            right = 1
        
        curtMax = max(left, right)
        self.res = max(self.res, curtMax)
        
        return curtMax