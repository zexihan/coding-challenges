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
private:
    ListNode* reverseLinkedList(ListNode* head, int k) {
        ListNode* newHead;
        ListNode* ptr = head;
        while (k--) {
            ListNode* nextNode = ptr->next;
            ptr->next = newHead;
            newHead = ptr;
            ptr = nextNode;
        }
        return newHead;
    }
    
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        int count = 0;
        ListNode* ptr = head;
        while (count < k && ptr) {
            ptr = ptr->next;
            count++;
        }
        
        if (count == k) {
            ListNode* reversedHead = reverseLinkedList(head, k);
            head->next = reverseKGroup(ptr, k);
            return reversedHead;
        }
        return head;
    }
};