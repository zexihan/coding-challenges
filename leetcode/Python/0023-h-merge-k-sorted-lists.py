# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Linked List
Use heap
Time: O(Nlogk)
Space: O(n), O(k)
"""
import heapq
class Solution_1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        move = head
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i))
        while heap:
            curVal, curIdx = heapq.heappop(heap)
            curHead = lists[curIdx]
            curNext = curHead.next
            move.next = curHead
            move = move.next
            if curNext:
                lists[curIdx] = curNext
                heapq.heappush(heap, (curNext.val, curIdx))
        return head.next

"""
Divide and Conquer
Merge sort
Time: O(Nlogk)
Space: O(1)
"""
class Solution_2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        dummy = ListNode(0)
        curt = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curt.next = l1
                l1 = l1.next
            else:
                curt.next = l2
                l2 = l2.next
            curt = curt.next
        if not l1:
            curt.next = l2
        else:
            curt.next = l1
        return dummy.next
