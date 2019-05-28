# DP
class Solution_1:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        f = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                # f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
                # f[0] = grid[0][0]
                if i == 0 and j == 0:
                    f[i][j] = grid[i][j]
                    continue
                t = float("inf")
                if i > 0:
                    t = min(t, f[i-1][j])
                if j > 0:
                    t = min(t, f[i][j-1])
                f[i][j] = t + grid[i][j]
        return f[m-1][n-1]


class Solution_2:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        # create 2 rows of arrays
        m, n = len(grid), len(grid[0])
        f = [[0 for i in range(n)] for j in range(2)]

        # two pointers
        # where is row i stored: now
        # where is row i-1 stored: old (old = 1 - now)
        old, now = 0, 0
        for i in range(m):
            old = now
            now = 1 - now  # 0->1, 1->0
            for j in range(n):
                # f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
                # f[0] = grid[0][0]
                if i == 0 and j == 0:
                    f[now][j] = grid[i][j]
                    continue
                t = float("inf")
                if i > 0:
                    t = min(t, f[old][j])
                if j > 0:
                    t = min(t, f[now][j-1])
                f[now][j] = t + grid[i][j]
        return f[now][n-1]
