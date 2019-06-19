# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
successor: one step right and then always left
predecessor: one step left and then always right

Algorithm
* If key > root.val then the node to delete is in the right subtree 
  root.right = deleteNode(root.right, key)
* If key < root.val then the node to delete is in the left subtree
  root.left = delteNode(root.left, key)
* If key == root.val then the node to delete is right here. Let's do it
  ** If the node is a leaf, the delete process is straightforward: root = null
  ** If the node is not a leaf and has the right child, then replace the node 
     value by a successor value root.val = successor.val, and then recursively
     delete the successor in the right subtree root.right = deleteNode(root.right,
     root.val)
  ** If the node is not a leaf and has only the left child, then replace the node
     value by a predecessor value root.val = predecessor.val, and then recursively 
     delete the predecessor in the left subtree root.left = deleteNode(root.left, 
     root.val)
"""
class Solution:
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root