# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Recursion - Divide and Conquer
Time: O(n^2)
Space: O(n^2)
"""
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.count = collections.defaultdict(int)
        self.res = []
        self.collect(root)
        return self.res

    def collect(self, node):
        if not node:
            return "#"
        serial = "{},{},{}".format(node.val, self.collect(node.left), self.collect(node.right))
        self.count[serial] += 1
        if self.count[serial] == 2:
            self.res.append(node)
        return serial