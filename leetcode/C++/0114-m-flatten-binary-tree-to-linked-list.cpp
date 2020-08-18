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
class Solution {
public:
    void flatten(TreeNode* root) {
        flattenTree(root);
    }
    
    TreeNode* flattenTree(TreeNode* node) {
        if (!node) return nullptr;
        if (!node->left && !node->right) return node;
        TreeNode* leftTail = flattenTree(node->left);
        TreeNode* rightTail = flattenTree(node->right);

        if (leftTail) {
            leftTail->right = node->right;
            node->right = node->left;
            node->left = nullptr;
        }
        
        return rightTail ? rightTail : leftTail;
    }
};


// Stack
class Solution {
public:
    void flatten(TreeNode* root) {
        if (!root) return;
        stack<TreeNode *> stk;
    
        while (1) {
            if (root->right)
                stk.push(root->right);

            if (root->left) {
                root->right = root->left;
                root->left = nullptr;
            } else {
                if (stk.empty()) 
                    return;
                root->right = stk.top();
                stk.pop();
            }
            root = root->right;
        }
    }
};