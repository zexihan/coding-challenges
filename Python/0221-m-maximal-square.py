# Brute force
# Time: O((mn)^2)
# Spce: O(1)
class Solution_1:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        maxsqlen = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    k = 1
                    flag = True
                    while k < rows - i and k < cols - j and flag:
                        for r in range(i, i + k + 1):
                            if matrix[r][j+k] == '0':
                                flag = False
                                break
                        for c in range(j, j + k + 1):
                            if matrix[i+k][c] == '0':
                                flag = False
                                break
                        if flag:
                            k += 1
                    if maxsqlen < k:        
                        maxsqlen = k
        return maxsqlen * maxsqlen

# DP
# Time: O(mn)
# Space: O(mn)
class Solution_2:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for c in range(cols + 1)] for r in range(rows+ 1)]
        maxsqlen = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    maxsqlen = max(maxsqlen, dp[i][j])
        return maxsqlen * maxsqlen


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
instance = Solution_2()
print(instance.maximalSquare(matrix))