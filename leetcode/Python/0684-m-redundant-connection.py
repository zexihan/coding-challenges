"""
DFS
Time: O(N^2)
Space: O(N)
"""
import collections
class Solution_1:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                for nei in graph[source]:
                    if dfs(nei, target):
                        return True

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)

"""
Union Find
* Path compression involves changing the x = parent[x] in the find function to 
  parent[x] = find(parent[x]). Basically, as we compute the correct leader for x, 
  we should remember our calculation.
* Union-by-rank involves distributing the workload of find across leaders evenly. 
  Whenever we dsu.union(x, y), we have two leaders xr, yr and we have to choose 
  whether we want parent[x] = yr or parent[y] = xr. We choose the leader that has a 
  higher following to pick up a new follower.
  Specifically, the meaning of rank is that there are less than 2 ^ rank[x] followers 
  of x. This strategy can be shown to give us better bounds for how long the recursive 
  loop in dsu.find could run for.
Time: O(N)
Space: O(N)
"""
class Solution_2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [-1] * 1001
        self.rank = [0] * 1001
        for edge in edges:
            if not self.union(*edge):
                return edge

    def find_parent(self, i):
        # path compression
        path = []
        while self.parent[i] != -1:
            path.append(i)
            i = self.parent[i]
        for p in path:
            self.parent[p] = i
        return i

    def union(self, x, y):
        # union-by-rank
        xr, yr = self.find_parent(x), self.find_parent(y)
        if xr == yr:
            return False
        elif self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True
