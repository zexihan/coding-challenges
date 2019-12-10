"""
DFS
Time: O(n^2)
Space: O(n)
"""
class Solution_1:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(M, curr, n):
            for i in range(n):
                if M[curr][i] == 1:
                    M[curr][i] = M[i][curr] = 0
                    dfs(M, i, n)

        n = len(M)
        res = 0
        for i in range(n):
            if M[i][i] == 1:
                res += 1
                dfs(M, i, n)

        return res

"""
Union Find
"""
class Solution_2:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        parent = [-1] * n
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1 and i != j:
                    self.union(parent, i, j)
        res = 0
        for i in range(n):
            if parent[i] == -1:
                res += 1
        return res

    def find_parent(self, parent, i):
        path = []
        while parent[i] != -1:
            path.append(i)
            i = parent[i]

        for p in path:
            parent[p] = i

        return i

    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        if x_set != y_set:
            parent[x_set] = y_set
