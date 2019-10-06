class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for i in range(n)]
        nums = [i for i in range(1, n*n+1)]
        seen = [[False] * n for i in range(n)]
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        cr, cc, r, c, di = 0, 0, 0, 0, 0
        for i in range(n*n):
            res[r][c] = nums[i]
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < n and 0 <= cc < n and seen[cr][cc] == False:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return res