/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) 
            return true;
        
        int left = getHeight(root.left);
        int right = getHeight(root.right);
        
        if (Math.abs(left - right) <= 1)
            return isBalanced(root.left) && isBalanced(root.right);
        else
            return false;
        
    }
    
    public int getHeight(TreeNode node) {
        if (node == null)
            return 0;
        
        int left = getHeight(node.left);
        int right = getHeight(node.right);
        
        return Math.max(left, right) + 1;
    }
}