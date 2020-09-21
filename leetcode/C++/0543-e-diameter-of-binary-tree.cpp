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
    int dfs(TreeNode* root, int& res) {
        if (!root) return 0;
        int L = dfs(root->left, res);
        int R = dfs(root->right, res);
        res = max(res, L + R + 1);
        return max(L, R) + 1;
    }
    
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int res = 1;
        dfs(root, res);
        return res - 1;
    }
};