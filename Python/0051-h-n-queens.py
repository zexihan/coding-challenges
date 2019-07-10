"""
DFS
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0:
            return []
        res = []
        self.solveNQueensCore(res, [0] * n, n, 0)
        return res

    def solveNQueensCore(self, res, row, n, idx):
        if idx == n:
            singleRes = self.translateString(row)
            res.append(singleRes)
            return

        for i in range(n):
            if self.isValid(row, idx, i):
                row[idx] = i
                self.solveNQueensCore(res, row, n, idx + 1)
                row[idx] = 0

    def translateString(self, row):
        resList = []
        for i in range(len(row)):
            sb = ""
            for j in range(len(row)):
                if j == row[i]:
                    sb += 'Q'
                else:
                    sb += '.'
            resList.append(sb)
        return resList

    def isValid(self, row, rowNum, colNum):
        for i in range(rowNum):
            if row[i] == colNum:
                return False
            if abs(row[i] - colNum) == abs(i - rowNum):
                return False
        return True
