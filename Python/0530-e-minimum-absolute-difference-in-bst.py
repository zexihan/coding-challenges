# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
    def getMinimumDifference(self, root: TreeNode) -> int:
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        res = float('inf')
        prev, cur = -1, -1
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                if prev == -1:
                    prev = stack[-1].val
                else:
                    cur = stack[-1].val
                    res = min(res, abs(cur - prev))
                    prev = cur
        return res

class Solution_2:
    def getMinimumDifference(self, root: TreeNode) -> int:
        l = []
        self.inorder(root, l)
        return min(abs(a - b) for a, b in zip(l, l[1:]))
    
    def inorder(self, node, l):
        if not node:
            return
        self.inorder(node.left, l)
        l.append(node.val)
        self.inorder(node.right, l)