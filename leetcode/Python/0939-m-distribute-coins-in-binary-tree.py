# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
DFS
If the leaf of a tree has 0 coins (an excess of -1 from what it needs), 
then we should push a coin from its parent onto the leaf. If it has say, 
4 coins (an excess of 3), then we should push 3 coins off the leaf.
Time: O(N)
Space: O(H)
"""
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node: 
            return 0
        L, R = self.dfs(node.left), self.dfs(node.right)
        self.res += abs(L) + abs(R)
        return node.val + L + R - 1
