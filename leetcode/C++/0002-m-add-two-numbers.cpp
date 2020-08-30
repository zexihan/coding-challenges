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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* p = l1, * q = l2, * cur = dummy; 
        int sum = 0, carry = 0;
        int a = 0, b = 0;
        while (p || q) {
            a = p ? p->val : 0;
            b = q ? q->val : 0;
            sum = carry + a + b;
            carry = sum / 10;
            cur->next = new ListNode(sum % 10);
            cur = cur->next;
            if (p) p = p->next;
            if (q) q = q->next;
        }
        if (carry > 0)
            cur->next = new ListNode(carry);
        return dummy->next;
    }
};