# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n)
# Space: O(h)
"""
DFS Recursion
If the current (sub)tree contains both p and q, then the function result is their LCA. 
If only one of them is in that subtree, then the result is that one of them. 
If neither are in that subtree, the result is null/None/nil.

我们可以用深度优先搜索，从叶子节点向上，标记子树中出现目标节点的情况。如果子树中有目标节点，标记
为那个目标节点，如果没有，标记为null。显然，如果左子树、右子树都有标记，说明就已经找到最小公共祖
先了。如果在根节点为p的左右子树中找p、q的公共祖先，则必定是p本身。

换个角度，可以这么想：如果一个节点左子树有两个目标节点中的一个，右子树没有，那这个节点肯定不是最
小公共祖先。如果一个节点右子树有两个目标节点中的一个，左子树没有，那这个节点肯定也不是最小公共祖
先。只有一个节点正好左子树有，右子树也有的时候，才是最小公共祖先。
"""
class Solution_1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 发现目标节点则通过返回值标记该子树发现了某个目标结点
        if root in (None, p, q): return root
        # 查看左子树中是否有目标结点，没有为null
        left = self.lowestCommonAncestor(root.left, p, q)
        # if left and left not in (p, q): return left
        # 查看右子树是否有目标节点，没有为null
        right = self.lowestCommonAncestor(root.right, p, q)
        # if right and right not in (p, q): return right
        # if 都不为空，说明左右子树都有目标结点，则公共祖先就是本身
        # else 如果发现了目标节点，则继续向上标记为该目标节点
        return root if left and right else left or right

"""
Iteration
I do a post-order traversal with a stack. 
Each stack element at first is a [node, parent] pair, where parent is the stack element of the node's parent node. 
When the children of a parent get finished, their results are appended to their parent's stack element. 
So when a parent gets finished, we have the results of its children/subtrees available 
(its stack element at that point is [node, parent, resultForLeftSubtree, resultForRightSubtree]).
"""
class Solution_2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        answer = []
        stack = [[root, answer]]
        while stack:
            top = stack.pop()
            (node, parent), subs = top[:2], top[2:]
            if node in (None, p, q):
                parent += node
            elif not subs:
                stack += top, [node.right, top], [node.left, top]
            else:
                parent += node if all(subs) else max(subs)
        return answer[0]
