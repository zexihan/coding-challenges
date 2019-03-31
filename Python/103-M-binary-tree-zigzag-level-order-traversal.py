# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preOrder(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            if level % 2 == 0: 
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.preOrder(root.left, level + 1, res)
            self.preOrder(root.right, level + 1, res)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.preOrder(root, 0, res)
        return res
        
        
        
