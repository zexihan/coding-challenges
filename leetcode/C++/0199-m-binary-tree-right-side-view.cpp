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
// DFS
// Time: O(N)
// Space: O(H)
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if (!root)
            return res;
        helper(root, 0, res);
        return res;
    }
    
    void helper(TreeNode* root, int level, vector<int>& res) {
        if (level == res.size())
            res.push_back(root->val);
        
        if (root->right) 
            helper(root->right, level + 1, res);
        if (root->left)
            helper(root->left, level + 1, res);
    }
};

// BFS
// Time: O(N)
// Space: O(D)
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if (!root)
            return res;
        
        queue<TreeNode*> nextLevel;
        nextLevel.push(root);
        queue<TreeNode*> curLevel;
        
        TreeNode* node;
        while (!nextLevel.empty()) {
            curLevel = nextLevel;
            
            while (!nextLevel.empty()) nextLevel.pop();
            
            while(!curLevel.empty()) {
                node = curLevel.front();
                curLevel.pop();
                
                if (node->left)
                    nextLevel.push(node->left);
                if (node->right)
                    nextLevel.push(node->right);
            }
            
            if (curLevel.empty())
                res.push_back(node->val);
        }
        return res;
    }
};