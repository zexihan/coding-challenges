/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    unordered_map<TreeNode*, TreeNode*> parent;
    set<TreeNode*> visited;
    vector<int> res;
    
    void findParent(TreeNode* root) {
        if (!root) return;
        if (root->left) {
            parent[root->left] = root;
            findParent(root->left);
        }
        if (root->right) {
            parent[root->right] = root;
            findParent(root->right);
        }
    }
    
    void dfs(TreeNode* node, int K) {
        if (!node) return;
        if (visited.find(node) != visited.end()) return;
        visited.insert(node);
        if (K == 0) {
            res.push_back(node->val);
            return;
        }
        dfs(node->left, K - 1);
        dfs(node->right, K - 1);
        dfs(parent[node], K - 1);
    }
    
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        if (!root) return res;
        findParent(root);
        dfs(target, K);
        return res;
    }
};