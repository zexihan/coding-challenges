"""
Prefix Sum and Binary Search
Time: O(N) preprocessing, O(logN) pick
Space: O(N)
"""
import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.N = len(rects)
        areas = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
        self.preSum = [0] * self.N
        self.preSum[0] = areas[0]
        for i in range(1, self.N):
            self.preSum[i] = self.preSum[i - 1] + areas[i]
        self.total = self.preSum[-1]
    
    def pickRect(self):
        rand = random.randint(0, self.total - 1)
        lo, hi = 0, self.N - 1
        while lo != hi:
            mid = (lo + hi) // 2
            if rand >= self.preSum[mid]:
                lo = mid + 1
            else:
                hi = mid
        return hi
    
    def pickPoint(self, rect):
        x1, y1, x2, y2 = rect
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return x, y

    def pick(self) -> List[int]:
        rectIndex = self.pickRect()
        rect = self.rects[rectIndex]
        return self.pickPoint(rect)


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
