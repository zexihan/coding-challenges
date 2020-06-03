class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        vector<int> result;
        stack<const TreeNode *> s;

        const TreeNode *p = root, *q = nullptr;

        do {
            while (p!= nullptr) {
                s.push(p);
                p = p->left;
            }
            q = nullptr;
            while (!s.empty()) {
                p = s.top();
                s.pop();
                if (p->right == q) {
                    result.push_back(p->val);
                    q = p;
                } else {
                    s.push(p);
                    p = p->right;
                    break;
                }
            }
        } while (!s.empty());

        return result;
    }
};

class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        vector<int> result;

        if (root == nullptr)
            return result;

        stack<const TreeNode *> s;
        const TreeNode *p = root;
        s.push(p);

        while (!s.empty()) {
            p = s.top();
            s.pop();
            result.push_back(p->val);
            if (p->left != nullptr)
                s.push(p->left);
            if (p->right != nullptr)
                s.push(p->right);
        }

        reverse(result.begin(), result.end());

        return result;
    }
};