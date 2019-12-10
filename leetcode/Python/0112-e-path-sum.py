# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Recursion without helper
"""
class Solution_1:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.val == sum:
            if not root.left and not root.right:
                return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

"""
Recursion with helper
"""
class Solution_2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self.helper(root, 0, sum)
    
    def helper(self, root, pathSum, sum):
        if not root:
            return False
        
        pathSum += root.val
        if not root.left and not root.right:
            return pathSum == sum
        
        left = self.helper(root.left, pathSum, sum)
        right = self.helper(root.right, pathSum, sum)
        
        return left or right