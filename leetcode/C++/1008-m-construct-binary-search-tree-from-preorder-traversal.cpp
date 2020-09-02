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
// Recursion
// Time: O(n)
// Space: O(n)
class Solution {
private:
    int idx = 0;
    vector<int> preorder;
        
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        this->preorder = preorder;
        return helper(INT_MIN, INT_MAX);
    }
    
    TreeNode* helper(int lower, int upper) {
        if (idx == preorder.size()) return nullptr;
        
        int val = preorder[idx];
        
        if (val < lower || val > upper) return nullptr;
        
        idx++;
        TreeNode* root = new TreeNode(val);
        root->left = helper(lower, val);
        root->right = helper(val, upper);
        return root;
    }
};

// Iteration using stack
// Time: O(n)
// Space: O(n)
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        int n = preorder.size();
        if (n == 0) return nullptr;
        
        TreeNode* root = new TreeNode(preorder[0]);
        stack<TreeNode*> stk;
        stk.push(root);
        
        for (int i = 1; i < n; i++) {
            TreeNode* node = stk.top();
            TreeNode* child = new TreeNode(preorder[i]);
            while (!stk.empty() && stk.top()->val < child->val) {
                node = stk.top();
                stk.pop();
            }
            if (node->val < child->val)
                node->right = child;
            else
                node->left = child;
            stk.push(child);
        }
        return root;
    }
};