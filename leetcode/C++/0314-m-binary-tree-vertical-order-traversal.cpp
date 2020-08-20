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
    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        
        map<int, vector<int>> mp;
        
        while (!q.empty()) {
            auto p = q.front();
            q.pop();
            TreeNode* nd = p.first;
            int col = p.second;
            mp[col].push_back(nd->val);
            if (nd->left) q.push({nd->left, col - 1});
            if (nd->right) q.push({nd->right, col + 1});
        }
        for (auto row : mp)
            res.push_back(row.second);
        return res;
    }
};