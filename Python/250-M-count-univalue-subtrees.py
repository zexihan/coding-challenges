# Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.count = 0

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root)
        return self.count
    
    def helper(self, root):
        if not root:
            return True
        flag_left = self.dfs(root.left)
        flag_right = self.dfs(root.right)
        if flag_left and flag_right \
        and (root.left == None or root.left.val == root.val) \
        and (root.right == None or root.right.val == root.val):
            self.count += 1
            return True
        else:
            return False