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
private:
    int dfs(TreeNode* r, int min_val = 100000, int max_val = 0) {
        if (r == nullptr) return max_val - min_val;
        max_val = max(max_val, r->val);
        min_val = min(min_val, r->val);
        return max(dfs(r->left, min_val, max_val), dfs(r->right, min_val, max_val));
    }
    
public:
    int maxAncestorDiff(TreeNode* root) {
        return dfs(root);
    }
};