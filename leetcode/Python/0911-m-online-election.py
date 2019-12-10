"""
Precomputed Answer + Binary Search
Time: O(N+QlogN), where N is the number of votes, and Q is the number of queries
Space: O(N)
"""
import collections
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.A = []
        count = collections.defaultdict(int)
        leader, m = None, 0

        for i in range(len(persons)):
            p, t = persons[i], times[i]
            count[p] += 1
            c = count[p]
            if c >= m:
                if p != leader:
                    leader = p
                    self.A.append((t, leader))

                if c > m:
                    m = c

    def q(self, t: int) -> int:
        lo, hi = 1, len(self.A)
        while lo < hi:
            mi = (lo + hi) // 2
            if self.A[mi][0] <= t:
                lo = mi + 1
            else:
                hi = mi
        return self.A[lo - 1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
