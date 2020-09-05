/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/

// DFS Inorder
class Solution {
private:
    Node* first;
    Node* last;
    void helper(Node* cur) {
        if (cur) {
            helper(cur->left);
            if (last) {
                last->right = cur;
                cur->left = last;
            } else {
                first = cur;
            }
            last = cur;
            helper(cur->right);
        }
    }
    
public:
    Node* treeToDoublyList(Node* root) {
        if (!root) return NULL;
        helper(root);
        first->left = last;
        last->right = first;
        return first;
    }
};