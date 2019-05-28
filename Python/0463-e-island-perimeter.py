class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        weight = len(grid[0]) if height else 0
        res = 0
        for h in range(height):
            for w in range(weight):
                if grid[h][w] == 1:
                    res += 4
                    if h > 0 and grid[h-1][w]:
                        res -= 2
                    if w > 0 and grid[h][w-1]:
                        res -= 2
        return res
