# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
dfs
当前node的高度是 1 + Max（height(node.left), height(node.right)
leaf的高度是 0
The height of a node is also its index in the result list (res).
"""
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if not root:
            return -1
        height = 1 + max(self.dfs(root.left, res), self.dfs(root.right, res))
        if len(res) < height + 1:
            res.append([])
        res[height].append(root.val)
        return height
