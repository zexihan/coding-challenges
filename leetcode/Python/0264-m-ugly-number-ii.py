"""
HashMap + Heap
{1, 2, 3, 4, 5, 6, 8, 9, 10, 12}
{2^0*3^0*5^0, 2^1*3^0*5^0, ...}
1
  2 3 5
    4 6 10
Time: O(nlogn)
Space: O(n)
"""
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        heap = [2, 3, 5]
        inHeap = set([2, 3, 5])
        primes = [2, 3, 5]

        for i in range(1, n):
            num = heapq.heappop(heap)
            for j in range(3):
                if primes[j] * num not in inHeap:
                    heapq.heappush(heap, primes[j] * num)
                    inHeap.add(primes[j] * num)
        return num

