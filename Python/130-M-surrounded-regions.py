# DFS
class Solution_1(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or board[x][y] != "O":
                return
            board[x][y] = "D"
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        if len(board) == 0:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(1, n - 1):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "D":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

# BFS
class Solution_2(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def fill(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or board[x][y] != "O":
                return
            queue.append((x, y))
            board[x][y] = "D"

        def bfs(x, y):
            if board[x][y] == "O": 
                fill(x, y)
            while queue:
                i, j = queue.pop(0)
                fill(i + 1, j)
                fill(i - 1, j)
                fill(i, j + 1)
                fill(i, j - 1)


        if len(board) == 0:
            return
        m, n = len(board), len(board[0])
        queue = []
        for i in range(n):
            bfs(0, i)
            bfs(m - 1, i)
        for j in range(1, m - 1):
            bfs(j, 0)
            bfs(j, n - 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "D":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
