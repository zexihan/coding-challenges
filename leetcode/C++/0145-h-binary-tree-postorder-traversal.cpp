class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
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