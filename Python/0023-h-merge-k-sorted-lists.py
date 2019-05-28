# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Time: O(Nlogk)
Space: O(n), O(k)
"""
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        move = head
        heap = []
        heapq.heapify(heap)
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