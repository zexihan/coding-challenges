"""
Hash Table
Time: O(n^2)
Space: O(n)
"""
import collections
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        N = len(A)
        abHash = collections.defaultdict(int)
        cdHash = collections.defaultdict(int)
        for i in range(N):
            for j in range(N):
                abHash[A[i] + B[j]] += 1
                cdHash[C[i] + D[j]] += 1

        res = 0
        for abSum in abHash:
            if -abSum not in cdHash:
                continue
            res += abHash[abSum] * cdHash[-abSum]
        return res
