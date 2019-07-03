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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) 
            return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while(q.size() > 0){
            List<Integer> list = new ArrayList<>();
            int size = q.size();
            for(int i = 0; i < size; i++){
                TreeNode node = q.poll();
                list.add(node.val);
                if(node.left != null) q.add(node.left);
                if(node.right != null) q.add(node.right);
            }
            res.add(0,list);
        }
        return res;
    }
}