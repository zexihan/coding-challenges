# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
reverse linked list
"""
class Solution_1:
    def plusOne(self, head: ListNode) -> ListNode:
        if not head:
            return head
        revHead = self.reverse(head)
        cur = revHead
        pre = cur
        carry = 1
        while cur:
            pre = cur
            tmp = cur.val + carry
            cur.val = tmp % 10
            carry = tmp // 10
            if carry == 0:
                break
            cur = cur.next
        if carry:
            pre.next = ListNode(1)
        return self.reverse(revHead)

    def reverse(self, head):
        if not head or not head.next:  # 边界条件
            return head
        cur = head  # 循环变量
        tmp = None  # 保存数据的临时变量
        newhead = None  # 新的翻转单链表的表头
        while cur:
            tmp = cur.next
            cur.next = newhead
            newhead = cur  # 更新 新链表的表头
            cur = tmp
        return newhead

"""
recursion
"""
class Solution_2:
    def plusOne(self, head: ListNode) -> ListNode:
        if not head:
            return head
        carry = self.helper(head)
        if carry == 1:
            res = ListNode(1)
            res.next = head
            return res
        return head
    
    def helper(self, node):
        if not node:
            return 1
        carry = self.helper(node.next)
        sum = node.val + carry
        node.val = sum % 10
        return sum // 10

"""
stack
"""
class Solution_3:
    def plusOne(self, head: ListNode) -> ListNode:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        carry = 1
        while len(stack) > 0 and carry:
            tmp = stack.pop()
            sum = tmp.val + carry
            tmp.val = sum % 10
            carry = sum // 10
        if carry:
            newHead = ListNode(1)
            newHead.next = head
            head = newHead
        return head
