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
    bool isValidBST(TreeNode* root) {
        if (!root)
            return true;
        return isValidNode(root, LONG_MIN, LONG_MAX);
    }
    
    bool isValidNode(TreeNode* root, long min, long max) {
        if (!root)
            return true;
        if (root->val >= max || root->val <= min)
            return false;
        return isValidNode(root->left, min, root->val) && isValidNode(root->right, root->val, max);
    }
};