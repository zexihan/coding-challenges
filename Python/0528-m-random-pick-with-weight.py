"""
Prefix Sum and Binary Search
Time: O(N) preprocessing, O(logN) pick
Space: O(N)
"""
import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.N = len(w)
        self.preSum = [0] * self.N
        self.preSum[0] = w[0]
        for i in range(self.N):
            self.preSum[i] = self.preSum[i - 1] + w[i]
        self.total = self.preSum[-1]

    def pickIndex(self) -> int:
        rand = random.randint(0, self.total - 1)
        lo, hi = 0, self.N - 1
        while lo != hi:
            mid = (lo + hi) // 2
            if rand >= self.preSum[mid]:
                lo = mid + 1
            else:
                hi = mid
        return hi


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
