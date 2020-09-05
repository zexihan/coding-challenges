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
    int findTilt(TreeNode* root) {
        int tilt = 0;
        treeSum(root, tilt);
        return tilt;
    }
    
    int treeSum(TreeNode* node, int& tilt) {
        if (!node) return 0;
        int left = treeSum(node->left, tilt);
        int right = treeSum(node->right, tilt);
        tilt += abs(left - right);
        return left + right + node->val;
    }
};