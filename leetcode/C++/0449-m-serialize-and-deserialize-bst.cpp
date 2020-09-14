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
private:
    void myserialize(TreeNode* root, string& s) {
        if (!root) return;
        s += to_string(root->val) + ",";
        myserialize(root->left, s);
        myserialize(root->right, s);
    }
    
    TreeNode* mydeserialize(string& data, int minV, int maxV) {
        if (data.length() == 0) return NULL;
        int pos = data.find(",");
        int val = stoi(data.substr(0, pos));
        if (val < minV || val > maxV) return NULL;
        
        TreeNode* node = new TreeNode(val);
        data = data.substr(pos + 1);
        node->left = mydeserialize(data, minV, val);
        node->right = mydeserialize(data, val, maxV);
        return node;
    }
    
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string s = "";
        if (!root) return s;
        myserialize(root, s);
        return s;
        
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == "") return NULL;
        return mydeserialize(data, INT_MIN, INT_MAX);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));