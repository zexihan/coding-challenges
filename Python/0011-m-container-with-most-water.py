"""
Time: O(n)
Space: O(1) 
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        maxm = 0
        j = 0
        k = size - 1
        while j < k:
            if height[j] <= height[k]:
                maxm = max(maxm, height[j] * (k - j))
                j += 1
            else:
                maxm = max(maxm, height[k] * (k - j))
                k -= 1
        return maxm
