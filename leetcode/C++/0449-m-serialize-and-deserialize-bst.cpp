/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (root == nullptr) return "";
        string s = "";
        myserialize(root, s);
        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == "") return nullptr;
        return mydeserialize(data, INT_MIN, INT_MAX);
    }

private:
    void myserialize(TreeNode* root, string& s) {
        if (root == nullptr) return;
        s += to_string(root->val) + ",";
        myserialize(root->left, s);
        myserialize(root->right, s);
    }
    
    TreeNode* mydeserialize(string& data, int min, int max) {
        if (data.size() == 0) 
            return nullptr;
        
        int pos = 0;
        int val = helper(data, pos);
        if (val < min || val > max)
            return nullptr;
        
        TreeNode* node = new TreeNode(val);
        
        data = data.substr(pos + 1);
        
        node->left = mydeserialize(data, min, node->val);
        node->right = mydeserialize(data, node->val, max);
        
        return node;
    }
    
    int helper(string& data, int& pos) {
        pos = data.find(",");
        int val = stoi(data.substr(0, pos));
        return val;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));