# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
BFS
"""
import collections
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = collections.deque([root])
        while q:
            res = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                res.append(node.val)
        return res[0]
            