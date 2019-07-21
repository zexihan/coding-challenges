"""
Heap + Greedy
Time: O(n)
Space: O(n)
https://blog.csdn.net/sunday0904/article/details/78174122
"""
import collections
import heapq
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        saved = collections.defaultdict(list)
        for num in nums:
            last = saved[num - 1]
            _len = 0 if not last else heapq.heappop(last)
            curt = saved[num]
            heapq.heappush(curt, _len + 1)
        for values in saved.values():
            for v in values:
                if v < 3:
                    return False
        return True
