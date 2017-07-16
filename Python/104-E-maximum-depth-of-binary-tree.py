# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS
class Solution_1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# BFS
from collections import deque
class Solution_2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return depth


if __name__ == "__main__":
    new_1 = Solution_1()
    new_2 = Solution_2()
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.right.left, root.right.right = TreeNode(15), TreeNode(7)
    root.right.left.left = TreeNode(10)
    print(new_1.maxDepth(root)) # 4
    print(new_2.maxDepth(root)) # 4