/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (!head || !head->next || m >= n)
            return head;
        
        ListNode* start = new ListNode(0);
        ListNode* end = new ListNode(0);
        
        start->next = head;
        end->next = head;
        
        // place start at one node behind from beginning of portion (m to n [m, n])
        for (int i = 0; i < m - 1; i++)
            start = start->next;
        // place end at last node of portion
        for (int i = 0; i < n; i++)
            end = end->next;
        
        ListNode* endJoint = end->next;
        ListNode* startJoint = start->next;
        
        end->next = nullptr;
        
        // reverse the portion in range [start->next, end]
        ListNode* cur = start;
        ListNode* prev = nullptr;
        while (cur) {
            ListNode* tmp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmp;
        }
        
        // join the reversed portion with initial list
        startJoint->next = endJoint;
        if (m != 1) {
            start->next = prev;
        } else {
            head = prev;
        }
        
        return head;
    }
};