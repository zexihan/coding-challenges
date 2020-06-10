class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int> &nums) {
        return helper(nums.begin(), nums.end());
    }
private:
    TreeNode *helper(vector<int>::const_iterator first, vector<int>::const_iterator last)
    {
        const auto length = distance(first, last);

        if (length <= 0) return nullptr;

        auto mid = first + length / 2;
        TreeNode* root = new TreeNode(*mid);
        root->left = helper(first, mid);
        root->right = helper(mid + 1, last);

        return root;
    }
};