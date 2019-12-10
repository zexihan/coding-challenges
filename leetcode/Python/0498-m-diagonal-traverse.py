"""
Time: O(mn)
space: O(1)
"""
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        cx, cy = 0, 0
        nx, ny = 0, 0
        dx, dy = -1, 1
        while True:
            if cx == m - 1 and cy == n - 1:
                res.append(matrix[cx][cy])
                return res
            res.append(matrix[cx][cy])
            nx, ny = cx + dx, cy + dy
            if ny >= n or (nx < m and ny < 0):
                nx, ny = cx + 1, cy  # down
                dx, dy = -dx, -dy
            elif nx >= m or nx < 0:
                nx, ny = cx, cy + 1  # right
                dx, dy = -dx, -dy
            cx, cy = nx, ny
