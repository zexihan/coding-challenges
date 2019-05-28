"""
bfs
"""
import collections
class Solution_1:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        
        topEdge = [(0, y) for y in range(n)]
        leftEdge = [(x, 0) for x in range(m)]
        pacific = set(topEdge + leftEdge)
        bottomEdge = [(m - 1, y) for y in range(n)]
        rightEdge = [(x, n - 1) for x in range(m)]
        atlantic = set(bottomEdge + rightEdge)
        
        self.bfs(pacific, matrix, m, n)
        self.bfs(atlantic, matrix, m, n)

        res = pacific & atlantic
        return [list(c) for c in res]
    
    def bfs(self, vset, matrix, m, n):
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = collections.deque(vset)
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if matrix[nx][ny] >= matrix[x][y]:
                        if (nx, ny) not in vset:
                            q.append((nx, ny))
                            vset.add((nx, ny))

"""
dfs
"""
class Solution_2:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]
        for i in range(m):
            self.dfs(p_visited, matrix, m, n, i, 0)
            self.dfs(a_visited, matrix, m, n, i, n - 1)
        for j in range(n):
            self.dfs(p_visited, matrix, m, n, 0, j)
            self.dfs(a_visited, matrix, m, n, m - 1, j)
        res = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, visited, matrix, m, n, x, y):
        visited[x][y] = True
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if matrix[nx][ny] >= matrix[x][y]:
                    if not visited[nx][ny]:
                        self.dfs(visited, matrix, m, n, nx, ny)
