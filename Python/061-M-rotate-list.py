# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # If the list is empty, just return the head
        if not head: 
            return head
        
        # Determine how much to rotate the list by if k is 
        # greater than the size of the list 
        l = self.getLength(head)
        rot =l-(k % l)-1
        
        # Determine the point where the rotation 
        # happens. 
        temp = head
        last = None 
        new_head = None 
        i = 0 
        while temp: 
            if i == rot:
                new_head = temp
                
            last = temp 
            temp = temp.next
            i += 1
            
        last.next = head
        head = new_head.next 
        new_head.next = None 
        
        return head
        
    def getLength(self,head):
        l = 0 
        while head: 
            l += 1 
            head = head.next 
        return l 