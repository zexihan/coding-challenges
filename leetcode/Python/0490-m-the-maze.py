"""
BFS
Time: O(mn)
Space: O(mn)
"""
import collections
class Solution_1:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[False for i in range(n)] for j in range(m)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = collections.deque()
        queue.append(start)
        visited[start[0]][start[1]] = True
        while queue:
            cx, cy = queue.popleft()
            if [cx, cy] == destination:
                return True
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                while nx >= 0 and ny >= 0 and nx < m and ny < n and maze[nx][ny] == 0:
                    nx += dx
                    ny += dy
                if not visited[nx - dx][ny - dy]:
                    queue.append([nx - dx, ny - dy])
                    visited[nx - dx][ny - dy] = True
        return False

"""
DFS
Time: O(mn)
Space: O(mn)
"""
class Solution_2:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = [[False for i in range(len(maze[0]))]
                   for j in range(len(maze))]
        return self.dfs(maze, start, destination, visited)
    
    def dfs(self, maze, start, destination, visited):
        if visited[start[0]][start[1]]:
            return False
        if start == destination:
            return True
        visited[start[0]][start[1]] = True
        r = start[1] + 1
        l = start[1] - 1
        u = start[0] - 1
        d = start[0] + 1
        # right
        while r < len(maze[0]) and maze[start[0]][r] == 0:
            r += 1
        if self.dfs(maze, [start[0], r - 1], destination, visited):
            return True
        # left
        while l >= 0 and maze[start[0]][l] == 0:
            l -= 1
        if self.dfs(maze, [start[0], l + 1], destination, visited):
            return True
        # up
        while u >= 0 and maze[u][start[1]] == 0:
            u -= 1
        if self.dfs(maze, [u + 1, start[1]], destination, visited):
            return True
        # down
        while d < len(maze) and maze[d][start[1]] == 0:
            d += 1
        if self.dfs(maze, [d - 1, start[1]], destination, visited):
            return True
        return False
