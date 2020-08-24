/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return NULL;
        
        unordered_map<Node*, Node*> mp;
        Node* nHead = new Node(head->val);
        mp[head] = nHead;
        Node* p = head;
        Node* q = nHead;
        while (p) {
            q->random = p->random;
            if (p->next) {
                q->next = new Node(p->next->val);
                mp[p->next] = q->next;
            }
            p = p->next;
            q = q->next;
        }
        q = nHead;
        while (q) {
            if (q->random)
                q->random = mp[q->random];
            q = q->next;
        }
        return nHead;     
    }
};