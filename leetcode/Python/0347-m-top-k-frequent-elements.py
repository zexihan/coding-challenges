"""
Heap
Time: O(Nlogk)
Space: O(N)
"""
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        return [heapq.heappop(heap)[1] for i in range(k)]
