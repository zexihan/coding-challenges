"""
Time: O(nlogn + n)
Space: O(n)
"""
class Solution_1:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        h = 0
        for i in range(n):
            h = max(h, min(n - i, citations[i]))
        return h

"""
Time: O(nlogn + logn)
Space: O(n)
"""
class Solution_2:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) / 2
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
        return n - l
