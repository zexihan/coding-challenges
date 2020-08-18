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
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0)
			return vector<TreeNode*>();
        return helper(1, n);
    }
    
    vector<TreeNode*> helper(int from, int to) {
        vector<TreeNode*> res;
        if (to < from) res.push_back(NULL);
        else if (to == from) res.push_back(new TreeNode(from));
        else {
            for (int i = from; i <= to; i++) {
                vector<TreeNode*> l = helper(from, i - 1);
                vector<TreeNode*> r = helper(i + 1, to);

                for (int j = 0; j < l.size(); j++) {
                    for (int k = 0; k < r.size(); k++) {
                        TreeNode* h = new TreeNode(i);
                        h->left = l[j];
                        h->right = r[k];
                        res.push_back(h);
                    }
                }
            }
        }
        return res;
    }
};