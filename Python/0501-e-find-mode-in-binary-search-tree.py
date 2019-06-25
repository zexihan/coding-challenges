# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        count = collections.Counter()
        self.inorder(root, count)
        maxCount = max(count.values())
        return [k for k, v in count.items() if v == maxCount]

    def inorder(self, node, count):
        if not node:
            return
        self.inorder(node.left, count)
        count[node.val] += 1
        self.inorder(node.right, count)
