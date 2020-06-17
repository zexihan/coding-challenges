class Solution_1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans

class Solution_2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        if not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        ans = [0] * (m*n)
        
        trace = [[False]*n for i in range(m)]
        x, y = 0, 0
        # direction: 0:right 1:down 2:left: 3:up
        direction = 0
        i = 1
        ans[0] = matrix[x][y]
        trace[0][0] = True
        while i < (m*n):
            bkup_x, bkup_y = x, y
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1

            if x < 0 or y < 0 or x >= m or y >= n or trace[x][y]:
                direction = (direction + 1) %4
                x, y = bkup_x, bkup_y
                continue

            ans[i] = matrix[x][y]
            trace[x][y] = True
            i += 1
        return ans