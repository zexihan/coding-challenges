# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
BFS
Time: O(n)
Space: O(n)
"""
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = [] 
        queue = collections.deque([root])
        while queue:
            curtLevel = []
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                curtLevel.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)       
            res.append(curtLevel)
        return res