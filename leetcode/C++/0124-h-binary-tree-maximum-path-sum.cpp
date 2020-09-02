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
    int max_sum = INT_MIN;
public:
    int maxPathSum(TreeNode* root) {
        max_gain(root);
        return max_sum;
    }
    
    int max_gain(TreeNode* node) {
        if (!node) return 0;
        int left_gain = max(max_gain(node->left), 0);
        int right_gain = max(max_gain(node->right), 0);
        
        int price_newpath = node->val + left_gain + right_gain;
        
        max_sum = max(max_sum, price_newpath);
        
        return node->val + max(left_gain, right_gain);
    }
};