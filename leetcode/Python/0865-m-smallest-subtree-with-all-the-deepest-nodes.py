# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Traverse + Divide and Conquer
Time: O(N)
Space: O(N)
"""
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.depths = {None: -1}
        self.dfs(root, None)
        self.maxDepth = max(self.depths.values())
        return self.commonAncestor(root)

    def dfs(self, node, parent=None):
        if node:
            self.depths[node] = self.depths[parent] + 1
            self.dfs(node.left, node)
            self.dfs(node.right, node)

    def commonAncestor(self, node):
        if not node or self.depths[node] == self.maxDepth:
            return node

        left = self.commonAncestor(node.left)
        right = self.commonAncestor(node.right)
        return node if left and right else left or right
