"""
DP
minpath[k][i]: the minimum path to level k position i from bottom to top
minpath[k][i] = min(minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i]
Since minpath[k][i] is used only once

For the kth level:
minpath[i] = min(minpath[i], minpath[i+1]) + triangle[k][i]

Time: O(n^2)
Space: O(n)
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]
        for layer in range(n - 2, -1, -1):
            for i in range(layer + 1):
                dp[i] = min(dp[i], dp[i+1]) + triangle[layer][i]
        return dp[0]