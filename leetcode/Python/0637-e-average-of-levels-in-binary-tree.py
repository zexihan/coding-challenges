# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        res = [] 
        queue = collections.deque([root])
        while queue:
            curtLevel = []
            for i in range(len(queue)):
                node = queue.popleft()
                curtLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)       
            res.append(sum(curtLevel) / len(curtLevel))
        return res