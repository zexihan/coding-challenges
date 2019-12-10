# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Recursion - traversal
Time: O(n)
Space: O(n)
"""
class Solution_1:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.helper(root, sum, [], res)
        return res
    
    def helper(self, root, sum, path, res):
        if not root.left and not root.right and sum == root.val:
            path.append(root.val)
            res.append(path)
        if root.left:
            self.helper(root.left, sum - root.val, path + [root.val], res)
        if root.right:
            self.helper(root.right, sum - root.val, path + [root.val], res)

"""
BFS
Time: O(n)
Space: O(n)
"""
class Solution_2:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val + curr.left.val, ls + [curr.left.val]))
            if curr.right:
                queue.append((curr.right, val + curr.right.val, ls + [curr.right.val]))
        return res