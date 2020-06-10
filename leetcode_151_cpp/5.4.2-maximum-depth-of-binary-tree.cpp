// recursive
// Time: O(n)
// Space: O(logn)
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;

        if (root->left == nullptr && root->right != nullptr)
            return maxDepth(root->right) + 1;
        if (root->left != nullptr && root->right == nullptr)
            return maxDepth(root->left) + 1;

        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};