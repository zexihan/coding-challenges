"""
Time: O(NlogN), where N is the length of stones
Space: O(N)
"""
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        p = list(range(20000))
        for x, y in stones:
            self.union(p, x, y + 10000)
        return N - len(set(self.find_parent(p, x) for x, y in stones))

    # find the subset of an element i
    def find_parent(self, parent, i):
        path = []
        while i != parent[i]:
            path.append(i)
            i = parent[i]

        for p in path:
            parent[p] = i

        return i

    # do union of two subsets
    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set
