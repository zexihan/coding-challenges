"""
dfs
Time: O(|V| + |E|)
"""
import collections
class Solution_1:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if i not in visited:
                res += self.dfs(graph, visited, i)
        return res
        
    def dfs(self, graph, visited, v):
        if v not in visited:
            visited.add(v)
            for node in graph[v]:
                self.dfs(graph, visited, node)
        return 1

"""
bfs
Time: O(|V| + |E|)
"""
import collections
class Solution_2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if i not in visited:
                res += self.bfs(graph, visited, [i])
        return res
    
    def bfs(self, graph, visited, q):
        for node in q:
            if node not in visited:
                q += graph[node]
                visited.add(node)
        return 1

"""
union find
Time: O(|V||E|)
"""
class Solution_3:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        parent = [-1] * n
        for u, v in edges:
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)
            if x != y:
                self.union(parent, x, y)
                res -= 1
        return res

    # find the subset of an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        else:
            return self.find_parent(parent, parent[i])

    # do union of two subsets
    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

