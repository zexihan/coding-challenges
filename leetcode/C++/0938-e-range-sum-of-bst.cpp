/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        if (!root) return 0;
        int res = 0;
        helper(root, res, L, R);
        return res;
    }
    
    void helper(TreeNode* root, int& res, int L, int R) {
        if (!root) return;
        if (root->val >= L && root->val <= R)
            res += root->val;
        if (root->val > L)
            helper(root->left, res, L, R);
        if (root->val < R)
            helper(root->right, res, L, R);
    }
};