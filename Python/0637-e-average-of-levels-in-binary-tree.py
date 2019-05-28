# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        ans = [] 
        queue = deque([root]) # queue, temporarily store nodes in each level
        while queue:
            tmpAns = [] # temporarily store node values in each level
            for i in range(len(queue)):
                cur = queue.popleft()
                tmpAns.append(cur.val)
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)       
            ans.append(sum(tmpAns) / len(tmpAns))
        return ans


if __name__ == "__main__":
    new = Solution()
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.right.left, root.right.right = TreeNode(15), TreeNode(7)
    print(new.averageOfLevels(root))