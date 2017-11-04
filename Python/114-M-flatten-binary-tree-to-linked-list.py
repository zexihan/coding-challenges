# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
class Solution_1(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.prev = root
        self.flatten(root.left)

        temp = root.right
        root.right, root.left = root.left, None
        self.prev.right = temp

        self.flatten(temp)

# Iterative
class Solution_2(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left and root.right:
                t = root.left
                while t.right:
                    t = t.right
                t.right = root.right
            
            if root.left:
                root.right = root.left
            root.left = None
            root = root.right