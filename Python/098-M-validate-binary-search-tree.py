# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time: O(n)
# Space: O(1)
"""
Recurse Down: Pass valid range down
helper(current_node, min, max)

Return Up: Current subTree is valid or not
current root & left & right

Current Level: Check current value is in the range
root.val < max & root.val > min
"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isValidNode(root, -float("inf"), float("inf"))
    
    def isValidNode(self, root, min, max):
        if not root:
            return True
        
        # current level: check root.val
        if root.val >= max or root.val <= min:
            return False

        # return left & right
        return self.isValidNode(root.left, min, root.val) and self.isValidNode(root.right, root.val, max)

if __name__ == "__main__":
    new = Solution()
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    print(new.isValidBST(root))