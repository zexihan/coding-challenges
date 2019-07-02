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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        preorder(root, res);
        return res;
    }
    
    public void preorder(TreeNode node, List<Integer> res) {
        if (node == null) 
            return;
        res.add(node.val);
        preorder(node.left, res);
        preorder(node.right, res);
    }
}

 /* 
  * Non-Recursion
  */
class Solution_2 {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();

        if (root == null)
            return res;

        stack.push(root);
        while (!stack.empty()) {
            TreeNode node = stack.pop();
            res.add(node.val);
            if (node.right != null)
                stack.push(node.right);
            if (node.left != null)
                stack.push(node.left);
        }
        return res;
    }
}