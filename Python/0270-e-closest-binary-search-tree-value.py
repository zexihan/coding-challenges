# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        min_d = float('inf')
        closest = root.val
        while root:
            if abs(target - root.val) < min_d:
                min_d = abs(target - root.val)
                closest = root.val
            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                return root.val
        return closest