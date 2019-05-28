# DP
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        for rowNum in range(rowIndex + 1):
            row = [0 for _ in range(rowNum + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = prevRow[j - 1] + prevRow[j]
            prevRow = row
        return row
