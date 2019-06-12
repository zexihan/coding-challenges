"""
Array
"""
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        k = 0
        res = 0
        for seat in seats:
            if seat == 0:
                k += 1
            else:
                res = max(res, (k + 1) // 2)
                k = 0
        return max(res, seats.index(1), seats[::-1].index(1))
