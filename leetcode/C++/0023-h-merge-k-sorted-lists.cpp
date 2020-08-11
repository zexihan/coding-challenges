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
// Heap
// Time: O(NlogK)
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto compare = [](ListNode* lhs, ListNode* rhs) { 
            return lhs->val > rhs->val; 
        };
        
        priority_queue<ListNode*, vector<ListNode*>, decltype(compare)> pq(compare);
        
        for (ListNode* node : lists) {
            if (node)
                pq.push(node);
        }
        
        ListNode* dummy = new ListNode();
        ListNode* cur = dummy;
        
        while (!pq.empty()) {
            ListNode* h = pq.top();
            pq.pop();
            cur->next = h;
            cur = cur->next;
            if (h->next) 
                pq.push(h->next);
        }
        
        return dummy->next;
    }
};

// Bottom-up
// Time: O(NlogK)
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0)
            return nullptr;
        
        while (lists.size() > 1) {
            vector<ListNode*> newLists;
            for (int i = 0; i + 1 < lists.size(); i += 2) {
                ListNode* mergedList = merge2lists(lists[i], lists[i+1]);
                newLists.push_back(mergedList);
            }
            if (lists.size() % 2 == 1)
                newLists.push_back(lists[lists.size() - 1]);
            lists = newLists;
        }
        
        return lists[0];
    }
    
    ListNode* merge2lists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();
        ListNode* cur = dummy;
        
        while (l1 && l2) {
            if (l1->val <= l2->val) {
                cur->next = l1;
                l1 = l1->next;
            } else {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        
        if (l1)
            cur->next = l1;
        else if (l2)
            cur->next = l2;
        
        return dummy->next;
    }
};

// Top down
// Time: O(NlogK)
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0)
            return nullptr;
        
        return mergeKListsHelper(lists, 0, lists.size() - 1);
    }
    
    ListNode* mergeKListsHelper(vector<ListNode*>& lists, int start, int end) {
        if (start == end) 
            return lists[start];
        
        int mid = start + (end - start) / 2;
        ListNode* left = mergeKListsHelper(lists, start, mid);
        ListNode* right = mergeKListsHelper(lists, mid + 1, end);
        return merge2lists(left, right);
    }
    
    ListNode* merge2lists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();
        ListNode* cur = dummy;
        
        while (l1 && l2) {
            if (l1->val <= l2->val) {
                cur->next = l1;
                l1 = l1->next;
            } else {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        
        if (l1)
            cur->next = l1;
        else if (l2)
            cur->next = l2;
        
        return dummy->next;
    }
};