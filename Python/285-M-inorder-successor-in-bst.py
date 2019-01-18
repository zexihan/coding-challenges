# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n)
# Space: O(1)
class Solution_1(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None
        while root != None and root.val != p.val:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        
        if root == None:
            return None
        
        if root.right == None:
            return successor
        
        root = root.right
        while root.left != None:
            root = root.left
        
        return root


class Solution_2(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None:
            return None
        
        successor = None
        while root is not None:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        
        return successor