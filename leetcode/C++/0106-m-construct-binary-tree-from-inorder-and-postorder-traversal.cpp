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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return buildTreeHelper(inorder, 0, inorder.size(), postorder, 0, postorder.size());
    }
    
    TreeNode* buildTreeHelper(vector<int>& inorder, int si, int ei, vector<int>& postorder, int sp, int ep) {
        if (sp == ep) return nullptr;
        TreeNode* root = new TreeNode(postorder[ep - 1]);
        int dis = find(inorder.begin()+si, inorder.begin() + ei, root->val) - inorder.begin() - si;
        root->left = buildTreeHelper(inorder, si, si+dis, postorder, sp, sp+dis);
        root->right = buildTreeHelper(inorder, si+dis+1, ei, postorder, sp+dis, ep-1);
        return root;
    }
};