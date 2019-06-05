"""
DFS
Time: O(2^n), n = 20 TLE
Space: O(n)
"""
class Solution_1:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)
        if s < S:
            return 0
        self.res = 0
        self.dfs(nums, 0, S)
        return self.res

    def dfs(self, nums, d, S):
        if d == len(nums):
            if S == 0:
                self.res += 1
            return
        self.dfs(nums, d + 1, S - nums[d])
        self.dfs(nums, d + 1, S + nums[d])
        
"""
DP
DP works because |V_n| <= S << O(2^n)

ways[i][j] # of ways to sum up to j using nums[0~i]

Transition 1: Push
Scan j for ways[i - 1]
ways[i][j - nums[i]] += ways[i - 1][j]
ways[i][j + nums[i]] += ways[i - 1][j]

Transition 2: Pull
Scan j for ways[i]
ways[i][j] = ways[i - 1][j - nums[i]] + ways[i - 1][j + nums[i]]

Init: ways[-1][0] = 1, one way to sum up 0, do nothing
Ans: ways[n - 1][S]

Time: O(n * sum)
Space: O(n * sum)
"""
class Solution_2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        s = sum(nums)
        if s < S:
            return 0
        offset = s
        ways = [[0 for i in range(s + offset + 1)] for j in range(n + 1)]
        ways[0][offset] = 1
        for i in range(n):
            for j in range(nums[i], 2 * s + 1 - nums[i]):
                if ways[i][j]:
                    ways[i + 1][j + nums[i]] += ways[i][j]
                    ways[i + 1][j - nums[i]] += ways[i][j]
        return ways[n][S + offset]
