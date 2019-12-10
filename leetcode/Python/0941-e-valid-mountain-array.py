"""
Array
Time: O(n)
Space: O(1)
"""
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        N = len(A)
        if N < 3:
            return False
        left = 0
        right = N - 1
        while left + 1 < N and A[left] < A[left + 1]:
            left += 1
        while right - 1 >= 0 and A[right] < A[right - 1]:
            right -= 1
        return left != 0 and right != N - 1 and left == right
