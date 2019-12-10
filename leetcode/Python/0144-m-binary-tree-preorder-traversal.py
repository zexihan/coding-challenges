# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Recursion
Time: O(n)
Space: O(n)
"""
class Solution_1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, node, res):
        if not node:
            return

        res.append(node.val)
        self.preorder(node.left, res)
        self.preorder(node.right, res)

        

"""
Non-Recursion
"""
class Solution_2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
