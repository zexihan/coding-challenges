# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: 
            return 0
        depth_left = depth_right = 0
        left = right = root 
        while left  : 
            left = left.left
            depth_left += 1
        while right : 
            right = right.right
            depth_right += 1
        if depth_left == depth_right: 
            return (1<<depth_left) - 1
        return  self.countNodes(root.left) + self.countNodes(root.right) + 1