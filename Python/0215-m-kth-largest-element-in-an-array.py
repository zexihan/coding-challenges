"""
Heap
Time: O((n-k)logk + k)
Space: O(k)
"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain a min heap with size k
        minHeap = []
        heapq.heapify(minHeap)
        # 1. add first k elems
        for i in range(k):
            heapq.heappush(minHeap, nums[i])
        # 2. add rest elems
        for i in range(k, len(nums)):
            if nums[i] > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[i])
        return heapq.heappop(minHeap)
