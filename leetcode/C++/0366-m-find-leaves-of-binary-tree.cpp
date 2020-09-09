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
    int dfs(TreeNode* node, unordered_map<int, vector<int>>& hash) {
        if (!node) return 0;
        int h = max(dfs(node->left, hash), dfs(node->right, hash)) + 1;
        hash[h].push_back(node->val);
        return h;
    }
    
public:
    vector<vector<int>> findLeaves(TreeNode* root) {
        unordered_map<int, vector<int>> hash;
        vector<vector<int>> res;
        int maxH = dfs(root, hash);
        for (int i = 1; i < maxH + 1; i++) 
            res.push_back(hash[i]);
        return res;
    }
};