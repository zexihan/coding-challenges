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
import collections
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        hash = collections.defaultdict(list)
        maxH = self.dfs(root, hash)

        for i in range(1, maxH + 1):
            res.append(hash[i])
        return res

    def dfs(self, cur, hash):
        if not cur:
            return 0

        h = max(self.dfs(cur.left, hash), self.dfs(cur.right, hash)) + 1
        hash[h].append(cur.val)

        return h
