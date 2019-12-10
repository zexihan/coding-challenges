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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, node, res):
        if not node:
            return
        self.inorder(node.left, res)
        res.append(node.val)
        self.inorder(node.right, res)

"""
Non-Recursion
"""
class Solution_2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        res = []
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                res.append(stack[-1].val)
        return res