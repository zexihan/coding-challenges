# DP
# f[i][j] = f[i-1][j] + f[i][j-1]
# f[0][0] = 1; f[i][0] = 1, f[0][j] = 1
# Time: O(mn)
# Space: O(mn)
class Solution_1:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [([0] * n) for i in range(m)]
        # top to bottom rowwise
        for i in range(m):
            # left to right columnwise
            for j in range(n):
                # init
                if i == 0 or j == 0:
                    f[i][j] = 1
                    continue
                f[i][j] = f[i-1][j] + f[i][j-1]
        
        return f[m-1][n-1]


class Solution_2:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ways = [0] * n
        ways[0] = 1
        for i in range(m) :
            for j in range(1, n) :
                ways[j] += ways[j-1]
        return ways[n-1]