# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

if __name__ == "__main__":
    new = Solution()
    t1 = TreeNode(1)
    t1.left, t1.right = TreeNode(3), TreeNode(2)
    t1.left.left = TreeNode(5)
    t2 = TreeNode(2)
    t2.left, t2.right = TreeNode(1), TreeNode(3)
    t2.left.right, t2.right.right = TreeNode(4), TreeNode(7)
    print(new.mergeTrees(t1,t2).left.right.val) # 4