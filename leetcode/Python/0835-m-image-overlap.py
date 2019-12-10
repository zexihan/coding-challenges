"""
Count by Delta
Time: O(n^4)
Space: O(n^2)
"""
import collections
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        count = collections.defaultdict(int)
        for i in range(M):
            for j in range(N):
                if A[i][j]:
                    for i2 in range(M):
                        for j2 in range(N):
                            if B[i2][j2]:
                                count[(i - i2, j - j2)] += 1
        return max(count.values() or [0])
