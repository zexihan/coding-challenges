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
 * Recursion - Divide and Conquer
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root == null)
            return true;
        return isValidNode(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    private boolean isValidNode(TreeNode root, long min, long max) {
        if (root == null)
            return true;
        if (root.val >= max || root.val <= min)
            return false;
        return isValidNode(root.left, min, root.val) && isValidNode(root.right, root.val, max);
    }
}