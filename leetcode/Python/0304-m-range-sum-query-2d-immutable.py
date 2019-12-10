"""
DP
Time: O(1)
Space: O(mn)
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return 
        m, n = len(matrix), len(matrix[0])
        self.rectSum = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.rectSum[i + 1][j + 1] = self.rectSum[i][j + 1] + \
                    self.rectSum[i + 1][j] + matrix[i][j] - self.rectSum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.rectSum[row2 + 1][col2 + 1] - self.rectSum[row1][col2 + 1] - \
            self.rectSum[row2 + 1][col1] + self.rectSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)