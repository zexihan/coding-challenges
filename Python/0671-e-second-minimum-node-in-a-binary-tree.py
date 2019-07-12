# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        self.min = root.val
        self.secondMin = float('inf')
        self.helper(root)
        return self.secondMin if self.secondMin != float('inf') else -1

    def helper(self, root):
        if not root:
            return
        if self.min < root.val < self.secondMin:
            self.secondMin = root.val
        elif root.val == self.min:
            self.helper(root.left)
            self.helper(root.right)
