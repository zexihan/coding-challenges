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
    private Map<Integer, Integer> count = new HashMap<>();
    private int max = 0;

    public int[] findMode(TreeNode root) {
        if (root == null)
            return new int[0];

        inorder(root);

        List<Integer> list = new ArrayList<>();
        for (int k : count.keySet()) {
            if (count.get(k) == max)
                list.add(k);
        }

        int[] res = new int[list.size()];
        for (int i = 0; i < list.size(); i++)
            res[i] = list.get(i);

        return res;
    }

    private void inorder(TreeNode node) {
        if (node == null)
            return;

        inorder(node.left);

        int cnt = count.getOrDefault(node.val, 0) + 1;
        max = Math.max(max, cnt);
        count.put(node.val, cnt);

        inorder(node.right);
    }
}