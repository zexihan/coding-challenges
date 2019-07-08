"""
DP
Time: O(n^2)
Space: O(n)
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [0] * n
        f[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: 
                    f[j] = 0
                elif j > 0: 
                    f[j] += f[j - 1]
        return f[n - 1]
