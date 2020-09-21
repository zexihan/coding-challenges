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
    int res = 0;
    int k;
    unordered_map<int, int> h;
    void preorder(TreeNode* node, int curSum) {
        if (!node) return;
        curSum += node->val;
        if (curSum == k)
            res++;
        res += h[curSum - k];
        h[curSum] = h[curSum] + 1;
        preorder(node->left, curSum);
        preorder(node->right, curSum);
        h[curSum] = h[curSum] - 1;
    }
    
public:
    int pathSum(TreeNode* root, int sum) {
        k = sum;
        preorder(root, 0);
        return res;
    }
};