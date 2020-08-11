# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        max_level = [0]
        self.res = []
        self.helper(root, 1, max_level)
        return self.res
    
    def helper(self, root, level, max_level):
        if root is None:
            return
        if max_level[0] < level:
            self.res.append(root.val)
            max_level[0] = level
        self.helper(root.right, level+1, max_level)
        self.helper(root.left, level+1, max_level)