// DFS

/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

class Solution {
    public:
        vector<int> rightSideView(TreeNode * root) {
            dfs(root, 0);
            return view;
        }

    private:
        vector<int> view;
        void dfs(TreeNode * node, int depth) {
            if (node != NULL) {
                if (depth == view.size())
                    view.push_back(node->val);
                dfs(node->right, depth + 1);
                dfs(node->left, depth + 1);
            }
        }
};