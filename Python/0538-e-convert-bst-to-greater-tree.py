# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.dfs(root)
        return root

    def dfs(self, cur):
        if not cur:
            return

        self.dfs(cur.right)
        self.sum += cur.val
        cur.val = self.sum
        self.dfs(cur.left)
