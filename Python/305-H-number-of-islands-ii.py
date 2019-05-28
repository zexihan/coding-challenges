"""
Union Find
"""
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = []
        island = set()
        self.size = 0
        self.parent = {}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for pos in positions:
            x, y = pos[0], pos[1]
            if (x, y) in island:
                res.append(self.size)
                continue
            
            island.add((x, y))
            self.parent[(x, y)] = (x, y)
            self.size += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) in island:
                    self.union((nx, ny), (x, y))
            res.append(self.size)
        return res
    
    def union(self, point_a, point_b):
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        if root_a != root_b:
            self.parent[root_a] = root_b
            self.size -= 1
    
    def find(self, point):
        path = []
        while point != self.parent[point]:
            path.append(point)
            point = self.parent[point]

        for p in path:
            self.parent[p] = point

        return point


