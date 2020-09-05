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
    vector<int> boundaryOfBinaryTree(TreeNode* root) {
        vector<int> res;
        if (!root) return res;
        res.push_back(root->val);
        
        vector<int> lefts, rights, leaves;
        
        getLeftBound(root->left, lefts);
        getLeaves(root->left, leaves);
        getLeaves(root->right, leaves);
        getRightBound(root->right, rights);
        reverse(rights.begin(), rights.end());
        
        for (int l : lefts) res.push_back(l);
        for (int leave : leaves) res.push_back(leave);
        for (int r : rights) res.push_back(r);
        
        return res;
    }
    
    void getLeftBound(TreeNode* node, vector<int>& lefts) {
        if (!node || (!node->left && !node->right)) return;
        lefts.push_back(node->val);
        if (node->left)
            getLeftBound(node->left, lefts);
        else
            getLeftBound(node->right, lefts);
    }
    
    void getLeaves(TreeNode* node, vector<int>& leaves) {
        if (!node) return;
        if (!node->left && !node->right)
            leaves.push_back(node->val);
        getLeaves(node->left, leaves);
        getLeaves(node->right, leaves);
    }
    
    void getRightBound(TreeNode* node, vector<int>& rights) {
        if (!node || (!node->left && !node->right)) return;
        rights.push_back(node->val);
        if (node->right)
            getRightBound(node->right, rights);
        else
            getRightBound(node->left, rights);
    }
};