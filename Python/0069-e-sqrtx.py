"""
Binary Search
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return -1
        elif x <= 1:
            return x

        start, end = 1, x
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid == x // mid:
                return mid
            if mid < x // mid:
                start = mid
            else:
                end = mid
        
        if end > x // end:
            return start
        return end
