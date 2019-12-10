"""
binary search, two pointers
Time: O(logn)
Space: O(1)
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if abs(x - arr[mid]) > abs(x - arr[mid + k]):
                left = mid + 1
            else:
                right = mid
        return arr[left: left + k]
