"""
DP
f[i][j] = f[i-1][j] + f[i][j-1]
f[0][0] = 1; f[i][0] = 1, f[0][j] = 1
Time: O(mn)
Space: O(mn)
"""
class Solution_1:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0 for j in range(n)] for i in range(m)]
        # top to bottom row-wise
        for i in range(m):
            # left to right column-wise
            for j in range(n):
                # init
                if i == 0 or j == 0:
                    f[i][j] = 1
                    continue
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        
        return f[m - 1][n - 1]

"""
DP
Time: O(mn)
Space: O(n)
"""
class Solution_2:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [0] * n
        ways[0] = 1
        for i in range(m) :
            for j in range(1, n) :
                ways[j] += ways[j - 1]
        return ways[n - 1]