# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        out = []

        def dfs(root, val):
            if not root:
                return
            if (not root.left) and (not root.right):
                out.append(val * 10 + root.val)
                return
            dfs(root.left, val * 10 + root.val)
            dfs(root.right, val * 10 + root.val)

        dfs(root, 0)
        return sum(out)
