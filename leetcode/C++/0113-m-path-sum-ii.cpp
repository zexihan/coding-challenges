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
// Time: O(N^2)
// Space: O(N)
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        if (!root) return res;
        helper(root, sum, vector<int>(), res);
        return res;
    }
    
    void helper(TreeNode* root, int sum, vector<int> path, vector<vector<int>>& res) {
        if (!root) return;
        if (root->val == sum && !root->left && !root->right) {
            path.push_back(root->val);
            res.push_back(path);
            return;
        }
        sum -= root->val;
        path.push_back(root->val);
        helper(root->left, sum, path, res);
        helper(root->right, sum, path, res);
    }
};