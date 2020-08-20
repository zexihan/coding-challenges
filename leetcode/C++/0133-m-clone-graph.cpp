/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node)
            return NULL;
        Node* nodeCopy = new Node(node->val);
        unordered_map<Node*, Node*> mp;
        mp[node] = nodeCopy;
        
        queue<Node*> q;
        q.push(node);
        while(!q.empty()) {
            Node* nd = q.front();
            q.pop();
            for (Node* nb : nd->neighbors) {
                if (mp.find(nb) == mp.end()) {
                    Node* nbCopy = new Node(nb->val);
                    mp[nb] = nbCopy;
                    mp[nd]->neighbors.push_back(nbCopy);
                    q.push(nb);
                } else {
                    mp[nd]->neighbors.push_back(mp[nb]);
                }
            }
        }
        return nodeCopy;
    }
};