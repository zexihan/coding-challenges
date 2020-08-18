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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return builTreeHelper(preorder, 0, preorder.size(), inorder, 0, inorder.size());
    }

    TreeNode* buildTreeHelper(vector<int>& preorder, int sp, int ep, vector<int>& inorder, int si, int ei) {
        if (sp == ep) return nullptr;
        TreeNode* root = new TreeNode(preorder[sp]);
        // number of nodes in left subtree
        int dis = find(inorder.begin()+si, inorder.begin() + ei, preorder[sp]) - inorder.begin() - si;
        root->left = buildTreeHelper(preorder, sp+1, sp+1+dis, inorder, si, si+dis);
        root->right = buildTreeHelper(preorder, sp+1+dis, ep, inorder, si+dis+1, ei);
        return root;
    }
};