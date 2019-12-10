# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
DP
rob_root = max(rob_left + rob_right, no_rob_left + no_rob_right + root.val)
no_rob_root = rob_left + rob_right
"""
class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.dfs_rob(root)[0]
    
    def dfs_rob(self, root):
        if not root:
            return 0, 0
        rob_left, no_rob_left = self.dfs_rob(root.left)
        rob_right, no_rob_right = self.dfs_rob(root.right)
        return max(rob_left + rob_right, no_rob_left + no_rob_right + root.val), rob_left + rob_right