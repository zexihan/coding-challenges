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
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        map<int, vector<pair<int , int>>> mp;
        queue<pair<TreeNode*, vector<int>>> q;
        q.push({root, {0, 0}});
        while (!q.empty()) {
            int row = q.front().second[0];
            int col = q.front().second[1];
            TreeNode* node = q.front().first;
            q.pop();
            mp[col].push_back({row, node->val});
            if (node->left)
                q.push({node->left, {row + 1, col - 1}});
            if (node->right)
                q.push({node->right, {row + 1, col + 1}});
        }
        vector<vector<int>> res;
        auto it = mp.begin();
        while (it != mp.end()) {
            sort(it->second.begin(), it->second.end());
            vector<int> res_col;
            for (auto p : it->second)
                res_col.push_back(p.second);
            res.push_back(res_col);
            it++;
        }
        return res;
    }
};