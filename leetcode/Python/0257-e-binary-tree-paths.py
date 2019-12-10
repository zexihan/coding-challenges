# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Recursion - Divide and Conquer
Time: O(N)
Space: O(N)
"""
class Solution_1:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        
        if not root:
            return paths
        
        if not root.left and not root.right:
            paths.append(str(root.val))
            return paths
        
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        
        for path in leftPaths:
            paths.append(str(root.val) + '->' + path)
        
        for path in rightPaths:
            paths.append(str(root.val) + '->' + path)
        
        return paths
        

"""
Recursion - Traverse
Time: O(N)
Space: O(N)
"""
class Solution_2:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # if reach a leaf
                    paths.append(path)  # update paths
                else:
                    path += '->'  # extend the current path
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)
        paths = []
        construct_paths(root, '')
        return paths

"""
Iterations
Time: O(N)
Space: O(N)
"""
class Solution_3:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return paths
