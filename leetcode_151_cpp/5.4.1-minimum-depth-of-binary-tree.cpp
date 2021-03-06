// recursive
// Time: O(n)
// Space: O(logn)
class Solution {
public:
    int minDepth(const TreeNode *root) {
        if (root == nullptr) return 0;

        if (root->left == nullptr && root->right != nullptr)
            return minDepth(root->right) + 1;
        if (root->left != nullptr && root->right == nullptr)
            return minDepth(root->left) + 1;

        return min(minDepth(root->left), minDepth(root->right)) + 1;
    }
};