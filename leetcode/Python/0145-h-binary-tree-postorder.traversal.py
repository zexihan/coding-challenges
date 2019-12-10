# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Recursion
"""
class Solution_1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.postorder(root, res)
        return res

    def postorder(self, node, res):
        if not node:
            return
        self.postorder(node.left, res)
        self.postorder(node.right, res)
        res.append(node.val)

"""
Non-Recursion
"""
class Solution_2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return res[::-1]
