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
    void inorder(TreeNode* node, vector<int>& nums) {
        if (!node) return;
        
        inorder(node->left, nums);
        nums.push_back(node->val);
        inorder(node->right, nums);
    }
    
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> nums;
        inorder(root, nums);
        return nums[k-1];
    }
};


class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> stk;
        TreeNode* cur = root;
        while (cur != NULL || !stk.empty()) {
            while (cur) {
                stk.push(cur);
                cur = cur->left;
            }
            cur = stk.top();
            stk.pop();
            if (--k == 0) return cur->val;
            cur = cur->right;
        }
        return 0;
    }
};