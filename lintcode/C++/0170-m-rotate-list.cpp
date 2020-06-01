/**
 * Definition of singly-linked-list:
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *        this->val = val;
 *        this->next = NULL;
 *     }
 * }
 */

class Solution {
public:
    ListNode * rotateRight(ListNode * head, int k) {
        if (head == NULL)
            return head;
        
        int len = 0;
        for (ListNode *node = head; node != NULL; node = node->next)
            len++;
        k = k % len;

        if (k == 0)
            return head;
        
        ListNode *fast = head;
        for (int i = 0; i < k; i++)
            fast = fast->next;
        
        ListNode *slow = head;
        while (fast->next != NULL) {
            slow = slow->next;
            fast = fast->next;
        }

        fast->next = head;
        head = slow->next;
        slow->next = NULL;

        return head;
    }
};