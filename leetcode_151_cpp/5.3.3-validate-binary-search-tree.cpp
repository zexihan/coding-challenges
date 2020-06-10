// Time: O(n)
// Sapce: O(logn)
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return helper(root, INT_MIN, INT_MAX);
    }
private:
    bool helper(TreeNode* root, int lower, int upper) {
        if (root == nullptr) return true;
        return root->val > lower && root->val < upper
            && isValidBST(root->left, lower, root->val)
            && isValidBST(root->right, root->val, upper);
    }
};