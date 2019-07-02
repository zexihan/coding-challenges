import java.util.Stack;

import javax.swing.tree.TreeNode;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

/*
 * Recursion
 */
class Solution_1 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        inorder(root, res);
        return res;
    }

    public void inorder(TreeNode node, List<Integer> res) {
        if (node == null)
            return;
        inorder(node.left, res);
        res.add(node.val);
        inorder(node.right, res);
    }
}

/*
 * Non-Recursion
 */
class Solution_2 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();

        if (root == null)
            return res;

        TreeNode dummy = new TreeNode(0);
        dummy.right = root;
        stack.push(dummy);

        while (!stack.empty()) {
            TreeNode node = stack.pop();
            if (node.right != null) {
                node = node.right;
                while (node != null) {
                    stack.push(node);
                    node = node.left;
                }
            }
            if (!stack.empty())
                res.add(stack.peek().val);
        }

        return res;
    }
}