"""
BFS
Time: O(m*n)
Space: O(m*n)
"""
import collections
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        q = collections.deque()
        visited = set()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and (x, y) not in visited:
                    q.append((x, y))
                    visited.add((x, y))
                    curtArea = 1
                    while q:
                        cx, cy = q.popleft()
                        for i in range(4):
                            nx, ny = cx + dx[i], cy + dy[i]
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in visited:
                                q.append((nx, ny))
                                visited.add((nx, ny))
                                curtArea += 1
                    res = max(res, curtArea)
        return res