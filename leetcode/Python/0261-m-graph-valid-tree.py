"""
bfs
"""
import collections
class Solution_1:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        q = collections.deque([0])
        while q:
            curr = q.popleft()
            visited.add(curr)
            for node in graph[curr]:
                if node not in visited:
                    visited.add(node)
                    q.append(node)
        
        return len(visited) == n

"""
dfs
"""
class Solution_2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        if not self.helper(0, -1, graph, visited):
            return False

        return len(visited) == n

    def helper(self, curr, parent, graph, visited):
        if curr in visited:
            return False
        visited.add(curr)
        for i in graph[curr]:
            if i != parent and not self.helper(i, curr, graph, visited):
                return False
        return True

"""
union find
"""
class Solution_3:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges) == n - 1:
            return False
        
        parent = [-1] * n
        for u, v in edges:
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)
            if x == y:
                return False
            else:
                self.union(parent, x, y)
        
        return True

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
