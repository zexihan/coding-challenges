# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
DFS - Divide and Conquer
"""
class Solution_1:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1

"""
DFS - Traverse
"""
class Solution_2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.depth = 0;
        self.helper(root, 1);
        return self.depth

    def helper(self, node, curDepth):
        if not node:
            return
        
        if curDepth > self.depth:
            self.depth = curDepth
        
        self.helper(node.left, curDepth + 1)
        self.helper(node.right, curDepth + 1)

"""
BFS
"""
import collections
class Solution_3:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 0
        queue = collections.deque([root])
        while queue:
            depth += 1
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return depth
