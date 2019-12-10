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
 * DFS - Divide and Conquer
 */
class Solution_1 {
    public int maxDepth(TreeNode root) {
        if (root == null)
            return 0;
            
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        
        return Math.max(left, right) + 1;
    }
}


/*
 * DFS - Traverse
 */
class Solution_2 {

    int depth;

    public int maxDepth(TreeNode root) {
        depth = 0;
        helper(root, 1);
        return depth;
    }

    public void helper(TreeNode node, int curDepth) {
        if (node == null) 
            return;
        
        if (curDepth > depth)
            depth = curDepth;
        
        helper(node.left, curDepth + 1);
        helper(node.right, curDepth + 1);
    }
}