"""
BFS
Time: O(MN)
Space: O(min(M, N))
"""
import collections
class Solution_1:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res += 1
                    q = collections.deque()
                    q.append((i, j))
                    grid[i][j] = '0'
                    while q:
                        x, y = q.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                                continue
                            if grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                q.append((nx, ny))
        return res


"""
Union Find
Time: O(MN)
Space: O(MN)
"""
class Solution_2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        self.res = 0
        self.parent = {}
        for x in range(n):
            for y in range(m):
                if grid[x][y] == '1':
                    self.parent[(x, y)] = (x, y)
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x in range(n):
            for y in range(m):
                if grid[x][y] == '1':
                    self.res += 1
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if grid[nx][ny] == '1':
                            self.union((nx, ny), (x, y))
        return self.res
    
    def union(self, point_a, point_b):
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        if root_a != root_b:
            self.parent[root_a] = root_b
            self.res -= 1
    
    def find(self, point):
        path = []
        while point != self.parent[point]:
            path.append(point)
            point = self.parent[point]

        for p in path:
            self.parent[p] = point

        return point
        

"""
DFS
Find an entrance of an island
Remove the island using DFS
Counting the number of removed islands
Time: O(MN)
Space: O(MN) 
"""
class Solution_3:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0

        count = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.removeIsland(grid, row, col, i, j)
                    count += 1
        return count

    def removeIsland(self, grid, row, col, x, y):
        grid[x][y] = '0'

        for i in range(-1,2):
            for j in range(-1, 2):
                if self.isValid(i, j, x, y, row, col) and grid[x + i][y + j] == '1':
                    self.removeIsland(grid, row, col, x + i, y + j)
    
    def isValid(self, i, j, x, y, row, col):
        return abs(i) != abs(j) and x + i >=0 and x + i < row and y + j >=0 and y + j < col
