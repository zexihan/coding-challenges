# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursion and DFS
class Solution_1(object):
    def preorder(self, root, level, ans):
        if root:
            if len(ans) < level + 1:
                ans.append([])
            ans[level].append(root.val)
            self.preorder(root.left, level + 1, ans)
            self.preorder(root.right, level + 1, ans)
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        self.preorder(root, 0, ans)
        return ans

# Time: O(n)
# Space: O(n)
# Queue, Iteration and BFS
from collections import deque
class Solution_2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
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
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)       
            ans.append(tmpAns)
        return ans


if __name__ == "__main__":
    new_1 = Solution_1()
    new_2 = Solution_2()
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.right.left, root.right.right = TreeNode(15), TreeNode(7)
    print(new_1.levelOrder(root))
    print(new_2.levelOrder(root))