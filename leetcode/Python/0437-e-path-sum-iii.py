# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
DFS (find starting node) + DFS (calculate num of paths)
"""
class Solution_1:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def dfs(self, root, sum):
        cnt = 0
        sum -= root.val
        if sum == 0:
            cnt += 1
        if root.left:
            cnt += self.dfs(root.left, sum)
        if root.right:
            cnt += self.dfs(root.right, sum)
        return cnt

"""
BFS (find starting node) + DFS (calculate num of paths)
"""
import collections
class Solution_2:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node:
                continue
            self.dfs(node, sum)
            q.append(node.left)
            q.append(node.right)
        return self.res

    def dfs(self, root, target):
        if not root:
            return
        target -= root.val
        if target == 0:
            self.res += 1
        self.dfs(root.left, target)
        self.dfs(root.right, target)