# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return None, None
        if root.val > V:
            bns = self.splitBST(root.left, V)
            root.left = bns[1]
            return bns[0], root
        else:
            bns = self.splitBST(root.right, V)
            root.right = bns[0]
            return root, bns[1]