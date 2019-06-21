# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
DFS
Let's calculate the depth of a node in the usual way: max(depth of node.left, 
depth of node.right) + 1. While we do, a path "through" this node uses 1 + 
(depth of node.left) + (depth of node.right) nodes. Let's search each node and 
remember the highest number of nodes used in some path. The desired length is 
1 minus this number.
Time: O(N)
Space: O(N)
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 1
        self.dfs(root)
        return self.res - 1
    
    def dfs(self, node):
        if not node:
            return 0
        L = self.dfs(node.left)
        R = self.dfs(node.right)
        self.res = max(self.res, L + R + 1)
        return max(L, R) + 1
