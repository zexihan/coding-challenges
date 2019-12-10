# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Reverse Linked List
"""
class Solution_1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        dummy = ListNode(0)
        head = dummy
        c = 0
        while l1 and l2:
            s = l1.val + l2.val + c
            c = 1 if s >= 10 else 0
            head.next = ListNode(s % 10)
            head = head.next
            l1, l2 = l1.next, l2.next
        l = l1 if l1 else l2
        while l:
            s = l.val + c
            c = 1 if s >= 10 else 0
            head.next = ListNode(s % 10)
            head = head.next
            l = l.next
        if c:
            head.next = ListNode(1)

        return self.reverse(dummy.next)
            
    def reverse(self, head):
        prev = None
        cur = head 
        while cur: 
            next = cur.next
            cur.next = prev 
            prev = cur 
            cur = next
        head = prev
        return head

"""
Add and Rebuild
"""
class Solution_2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        add = str(int(num1) + int(num2))
        head = ListNode(add[0])
        res = head
        for i in range(1, len(add)):
            node = ListNode(add[i])
            head.next = node
            head = head.next
        return res

"""
Stack
"""
class Solution_3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        res = None
        carry = 0
        while stack1 and stack2:
            add = stack1.pop() + stack2.pop() + carry
            carry = 1 if add >= 10 else 0
            temp = res
            res = ListNode(add % 10)
            res.next = temp
        l = stack1 if stack1 else stack2
        while l:
            add = l.pop() + carry
            carry = 1 if add >= 10 else 0
            temp = res
            res = ListNode(add % 10)
            res.next = temp
        if carry:
            temp = res
            res = ListNode(1)
            res.next = temp
        return res


