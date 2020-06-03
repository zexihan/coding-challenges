// Iterative with stack
// Time: O(n)
// Space: O(n)
class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> result;
        stack<const TreeNode *> s;
        if (root != nullptr)
            s.push(root);
        
        while (!s.empty()) {
            const TreeNode *p = s.top();
            s.pop();
            result.push_back(p->val);

            if (p->right != nullptr)
                s.push(p->right);
            if (p->left != nullptr)
                s.push(p->left);
        }
        return result;
    }
};

// Recursive
class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> result;
        helper(root, result);
        return result;
    }
private:
    void helper(TreeNode *root, vector<int> &result) {
        if (root == nullptr)
            return;
        result.push_back(root->val);
        helper(root->left, result);
        helper(root->right, result);
    }
};