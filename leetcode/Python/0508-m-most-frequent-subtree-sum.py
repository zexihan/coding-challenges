# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        sums = collections.Counter()
        self.getSum(root, sums)
        maxSum = max(sums.values())
        return [k for k, v in sums.items() if v == maxSum]

    def getSum(self, node, sums):
        if not node:
            return 0
        s = self.getSum(node.left, sums) + node.val + \
            self.getSum(node.right, sums)
        sums[s] += 1
        return s
