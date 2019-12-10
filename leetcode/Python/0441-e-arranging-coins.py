"""
Binary Search
Time: O(logn)
Space: O(1)
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid + mid ** 2 <= 2 * n:
                start = mid
            else:
                end = mid
        
        if start + start ** 2 <= 2 * n:
            return start
        return end