"""
BFS
"""
import collections
class Solution_1:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        q = collections.deque()
        q.append((sr, sc))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        color = image[sr][sc]
        if color == newColor:
            return image
        while q:
            cx, cy = q.popleft()
            image[cx][cy] = newColor
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if image[nx][ny] == color:
                    q.append((nx, ny))
        return image

"""
DFS
"""
class Solution_2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        color = image[sr][sc]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if color == newColor: 
            return image
        def dfs(x, y):
            if image[x][y] == color:
                image[x][y] = newColor
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue
                    dfs(nx, ny)
        dfs(sr, sc)
        return image
