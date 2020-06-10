// slow & fast pointers
// Time: O(n^2)
// Space: O(n)
class Solution {
public: 
    TreeNode* sortedListToBST(ListNode* head) {
        if (!head) return nullptr;
        return helper(head, nullptr);
    }
    
private:
    TreeNode* helper(ListNode* head, ListNode* tail) {
        if (head == tail) return nullptr;
        ListNode *slow = head, *fast = head;
        while (fast != tail && fast->next != tail) {
            slow = slow->next;
            fast = fast->next->next;
        }
        TreeNode *cur = new TreeNode(slow->val);
        cur->left = helper(head, slow);
        cur->right = helper(slow->next, tail);
        return cur;
    }
};

// top-down
// Time: O(n^2)
// Space: O(n)
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        return helper(head, listLength(head));
    }

private:
    TreeNode* helper(ListNode* head, int len) {
        if (len == 0) return nullptr;
        if (len == 1) return new TreeNode(head->val);

        TreeNode* root = new TreeNode(nth_node(head, len / 2 + 1)->val);
        root->left = helper(head, len / 2);
        root->right = helper(nth_node(head, len / 2 + 2), (len - 1) / 2);

        return root;
    }

    int listLength(ListNode* node) {
        int n = 0;

        while (node) {
            ++n;
            node = node->next;
        }

        return n;
    }

    ListNode *nth_node(ListNode* node, int n)
    {
        while (--n)
            node = node->next;

        return node;
    }
};

// bottom-up
// Time: O(n)
// Space: O(logn)
class Solution {
public:
    TreeNode* sortedListToBST(ListNode *head) {
        int len = 0;
        ListNode *p = head;
        while (p) {
            len++;
            p = p->next;
        }
        return helper(head, 0, len - 1);
    }

private:
    TreeNode* helper(ListNode*& list, int start, int end) {
        if (start > end) return nullptr;
        
        int mid = start + (end - start) / 2;
        TreeNode *leftChild = helper(list, start, mid - 1);
        TreeNode *parent = new TreeNode(list->val);
        parent->left = leftChild;
        list = list->next;
        parent->right = helper(list, mid + 1, end);
        return parent;
    }
};