class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode *root) {
        vector<vector<int>> result;
        traverse(root, 1, result);
        std::reverse(result.begin(), result.end());
        return result;
    }
private:
    void traverse(TreeNode *root, size_t level, vector<vector<int>> &result) {
        if (!root)
            return;
        
        if (level > result.size())
            result.push_back(vector<int>());
        
        result[level-1].push_back(root->val);
        traverse(root->left, level+1, result);
        traverse(root->right, level+1, result);
    }
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        queue<TreeNode *> q;

        if (root == nullptr)
            return result;
        else
            q.push(root);
        
        while (!q.empty()) {
            vector<int> level;
            size_t size = q.size();
            for (size_t i = 0; i < size; i++) {
                TreeNode *node = q.front();
                q.pop();
                level.push_back(node->val);
                if (node->left != nullptr)
                    q.push(node->left);
                if (node->right != nullptr)
                    q.push(node->right);
            }
            result.push_back(level);
        }
        reverse(result.begin(), result.end());
        return result;
    }
};