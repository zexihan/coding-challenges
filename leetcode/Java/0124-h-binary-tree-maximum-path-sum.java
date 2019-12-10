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
    private class ResultType {
        int root2any, any2any;
        ResultType(int root2any, int any2any) {
            this.root2any = root2any;
            this.any2any = any2any;
        }
    }

    private ResultType helper(TreeNode root) {
        if (root == null)
            return new ResultType(Integer.MIN_VALUE, Integer.MIN_VALUE);
        
        ResultType left = helper(root.left);
        ResultType right = helper(root.right);

        int root2any = Math.max(Math.max(left.root2any, right.root2any), 0) + root.val;

        int any2any = Math.max(left.any2any, right.any2any);

        any2any = Math.max(
            any2any,
            Math.max(left.root2any, 0) + root.val + Math.max(right.root2any, 0)
        );

        return new ResultType(root2any, any2any);
    }

    public int maxPathSum(TreeNode root) {
        ResultType res = helper(root);
        return res.any2any;
    }
}