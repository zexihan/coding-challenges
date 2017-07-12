# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
parent.left = leftchild -> leftchild.left = rightchild
parent.right = rightchild -> leftchild.right = parent

Start from leftmost leaf
Bottom up
Store all nodes along the path in stack
""" 
# Time: O(n)
# Spac: O(n)
class Solution_1:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype root: TreeNode
        """
        if not root:
            return root

        stack = []
        # append left nodes into stack
        while root:
            stack.append(root)
            root = root.left
        # set new root
        newRoot = stack.pop()
        cur = newRoot
        # change pointers
        while stack:
            oriParent = stack.pop()
            cur.right = oriParent
            cur.left = oriParent.right

            cur = oriParent
            oriParent.left = None
            oriParent.right = None
        
        return newRoot

"""
??? converted from java, suspicious result ???
Recursion:
    Identical Subproblem
    Lower Level First
"""
# Time: O(n)
# Spac: O(n)
class Solution_2:
    def upsideDownBinaryTree(self, root): 
        if not root or not root.left:
            return root
        # assumen all lower levels are handled
        newRoot = self.upsideDownBinaryTree(root.left)

        # handle current level
        root.left.left.left = root.right
        root.left.right = root

        root.left = None
        root.right = None

        return newRoot

# recursion, same as above, suspicious result
class Solution_3:
    def upsideDownBinaryTree(self, root):
        return self.upsideDownBinaryTreeRecu(root, None)
    
    def upsideDownBinaryTreeRecu(self, p, parent):
        if p is None:
            return parent
        
        root = self.upsideDownBinaryTreeRecu(p.left, p)
        if parent:
            p.left = parent.right
        else:
            p.left = None
        p.right = parent
        
        return root

if __name__ == "__main__":
    new_1 = Solution_1()
    new_2 = Solution_2()
    new_3 = Solution_3()
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    root.left.left, root.left.right = TreeNode(4), TreeNode(5)
    print(new_1.upsideDownBinaryTree(root).val)
    print(new_2.upsideDownBinaryTree(root).val)
    print(new_3.upsideDownBinaryTree(root).val)


