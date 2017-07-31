# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(n)
# Space: O(1)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = ListNode(0)
        dummy.next = cur
        carry = 0
        while True:
            if l1:
                cur.val += l1.val
                l1 = l1.next
            if l2:
                cur.val += l2.val
                l2 = l2.next
            
            cur.val += carry
            if cur.val >= 10:
                cur.val %= 10
                carry = 1
            else:
                carry = 0
            
            if l1 or l2 or carry:
                cur.next = ListNode(0)
                cur = cur.next
            else:
                break

        return dummy.next


if __name__ == "__main__":
    new = Solution()
    l1, l1.next, l1.next.next = ListNode(2), ListNode(4), ListNode(3)
    l2, l2.next, l2.next.next = ListNode(5), ListNode(6), ListNode(4)
    
    l3 = new.addTwoNumbers(l1, l2)
    for i in range(3):
        print(l3.val)
        l3 = l3.next