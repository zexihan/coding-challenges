"""
Sort by Count
Time: O(A(N + logA)), N - length of S, A - size of the alphabet
Space: O(N)
"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N + 1) / 2:
                return ""
            A.extend(c * x)
        res = [None] * N
        res[::2], res[1::2] = A[N//2:], A[:N//2]
        return "".join(res)