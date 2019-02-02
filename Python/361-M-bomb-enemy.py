class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        up = [[0 for i in range(n)] for j in range(m)]
        down = [[0 for i in range(n)] for j in range(m)]
        left = [[0 for i in range(n)] for j in range(m)]
        right = [[0 for i in range(n)] for j in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "W":
                    up[i][j] = 0
                    continue
                up[i][j] = 1 if grid[i][j] == "E" else 0
                if i > 0:
                    up[i][j] += up[i-1][j]

        # order
        for i in range(m-1, -1, -1):
            for j in range(n):
                if grid[i][j] == "W":
                    down[i][j] = 0
                    continue
                down[i][j] = 1 if grid[i][j] == "E" else 0
                if i < m - 1:
                    down[i][j] += down[i+1][j]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "W":
                    left[i][j] = 0
                    continue
                left[i][j] = 1 if grid[i][j] == "E" else 0
                if j > 0:
                    left[i][j] += left[i][j-1]

        for i in range(m):
            for j in range(n-1, -1, -1):
                if grid[i][j] == "W":
                    right[i][j] = 0
                    continue
                right[i][j] = 1 if grid[i][j] == "E" else 0
                if j < n - 1:
                    right[i][j] += right[i][j+1]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    t = up[i][j] + left[i][j] + down[i][j] + right[i][j]
                    res = max(t, res)

        return res
