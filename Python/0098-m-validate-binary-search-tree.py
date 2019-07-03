# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Recursion - Divide and Conquer
Time: O(n)
Space: O(1)
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isValidNode(root, float('-inf'), float('inf'))
    
    def isValidNode(self, cur, min, max):
        if not cur:
            return True
        if cur.val >= max or cur.val <= min:
            return False
        return self.isValidNode(cur.left, min, cur.val) and self.isValidNode(cur.right, cur.val, max)