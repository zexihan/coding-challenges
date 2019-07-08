"""
Recursion - Traversal
Time: O(2^n) - TLE
"""
class Solution_1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.best = float('inf')
        self.traverse(triangle, 0, 0, 0)
        return self.best

    def traverse(self, triangle, x, y, sum):
        if x == len(triangle):
            if sum < self.best:
                self.best = sum
            return
        self.traverse(triangle, x + 1, y, sum + triangle[x][y])
        self.traverse(triangle, x + 1, y + 1, sum + triangle[x][y])

"""
Recursion - Divide and Conquer
Time: O(2^n) - TLE
"""
class Solution_2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.divideConquer(triangle, 0, 0)
    
    # return minimum path from (x, y) to bottom
    def divideConquer(self, triangle, x, y):
        if x == len(triangle):
            return 0
        left = self.divideConquer(triangle, x + 1, y)
        right = self.divideConquer(triangle, x + 1, y + 1)
        return triangle[x][y] + min(left, right)

"""
Recursion - Divide and Conquer with Memorization
Time: O(n^2)
"""
import collections
class Solution_3:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.hash = collections.defaultdict(lambda: float('inf'))
        return self.divideConquer(triangle, 0, 0)

    # return minimum path from (x, y) to bottom
    def divideConquer(self, triangle, x, y):
        if x == len(triangle):
            return 0

        if self.hash[(x, y)] != float('inf'):
            return self.hash[(x, y)]
        
        left = self.divideConquer(triangle, x + 1, y)
        right = self.divideConquer(triangle, x + 1, y + 1)

        self.hash[(x, y)] = triangle[x][y] + min(left, right)
        return self.hash[(x, y)]

"""
DP - Bottom Up
minpath[k][i]: the minimum path to level k position i from bottom to top
minpath[k][i] = min(minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i]
Since minpath[k][i] is used only once

Time: O(n^2)
Space: O(n)
"""
class Solution_4:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[:]
        for layer in range(len(triangle) - 2, -1, -1):
            for i in range(layer + 1):
                dp[layer][i] = min(
                    dp[layer + 1][i], dp[layer + 1][i + 1]) + triangle[layer][i]
        return dp[0][0]
