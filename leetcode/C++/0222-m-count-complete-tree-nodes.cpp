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
    int computeDepth(TreeNode* node) {
        int d = 0;
        while (node->left) {
            node = node->left;
            ++d;
        }
        return d;
    }
    
    bool exists(int idx, int d, TreeNode* node) {
        int left = 0, right = pow(2, d) - 1;
        int mid;
        for (int i = 0; i < d; ++i) {
            mid = left + (right - left) / 2;
            if (idx <= mid) {
                node = node->left;
                right = mid - 1;
            } else {
                node = node->right;
                left = mid + 1;
            }
        }
        return node != NULL;
    }
    
    int countNodes(TreeNode* root) {
        if (!root) return 0;
        int d = computeDepth(root);
        
        if (d == 0) return 1;
        
        int left = 1, right = pow(2, d) - 1;
        int mid;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (exists(mid, d, root)) left = mid + 1;
            else right = mid - 1;
        }
        return pow(2, d) - 1 + left;
    }
};