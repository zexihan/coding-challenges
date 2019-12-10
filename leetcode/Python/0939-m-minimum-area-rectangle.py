"""
Sort by Column
Time: O(n^2)
Space: O(n)
"""
import collections
class Solution_1:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        res = float('inf')

        for x in sorted(columns):
            column = sorted(columns[x])
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[(y1, y2)]) * (y2 - y1))
                    lastx[(y1, y2)] = x
        return res if res < float('inf') else 0


"""
Count by Diagonal
Time: O(n^2)
Space: O(n)
"""
class Solution_2:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pSet = set(map(tuple, points))
        res = float('inf')
        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in pSet and (p2[0], p1[1]) in pSet:
                    res = min(res, abs((p1[0] - p2[0]) * (p1[1] - p2[1])))
        return res if res < float('inf') else 0
