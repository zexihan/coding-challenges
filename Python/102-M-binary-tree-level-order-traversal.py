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

# Iteration and BFS
class Solution_2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        ans = [[root.val]] 
        refList1 = [root] # work with refList2 for traversal
        while True:
            refList2 = [] # temporarily store nodes in each level
            tmpAns = [] # temporarily store node values in each level
            for i in range(len(refList1)):
                cur = refList1[i]
                if cur.left != None:
                    refList2.append(cur.left)
                    tmpAns.append(cur.left.val)
                if cur.right != None:
                    refList2.append(cur.right)
                    tmpAns.append(cur.right.val)
            if len(refList2) == 0:
                break
            ans.append(tmpAns)
            refList1 = refList2
        return ans


if __name__ == "__main__":
    new_1 = Solution_1()
    new_2 = Solution_2()
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.right.left, root.right.right = TreeNode(15), TreeNode(7)
    print(new_1.levelOrder(root))
    print(new_2.levelOrder(root))