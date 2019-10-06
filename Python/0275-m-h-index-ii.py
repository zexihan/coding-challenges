"""
Time: O(logn)
Space: O(1)
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) / 2
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
        return n - l
