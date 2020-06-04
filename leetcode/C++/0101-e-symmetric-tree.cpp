// Recursive
// Time: O(n)
// Space: O(logn)
class Solution {
public:
    bool isSymmetric(TreeNode *root) {
        if (root == nullptr) return true;
        return helper(root->left, root->right);
    }
private:
    bool helper(TreeNode *p, TreeNode *q) {
        if (p == nullptr && q == nullptr) return true;
        if (p == nullptr || q == nullptr) return false;
        return p->val == q->val && helper(p->left, q->right)
                                && helper(p->right, q->left);
    }
};

// Iterative
// Time: O(n)
// Space: O(logn)
class Solution{
    bool isSymmetric(TreeNode *root) {
        if (!root) return true;

        stack<TreeNode*> s;
        s.push(root->left);
        s.push(root->right);

        while (!s.empty()) {
            TreeNode *p = s.top(); s.pop();
            TreeNode *q = s.top(); s.pop();

            if (p == nullptr && q == nullptr) continue;
            if (p == nullptr || q == nullptr) return false;
            if (p->val != q->val) return false;

            s.push(p->left);
            s.push(q->right);

            s.push(p->right);
            s.push(q->left);
        }
        return true;
    }
};