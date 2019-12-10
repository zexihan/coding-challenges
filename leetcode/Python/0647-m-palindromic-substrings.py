"""
DP
dp[i][j] = 1 if i == j
dp[i][j] = s[i] == s[j] if j = i + 1
dp[i][j] = s[i] == s[j] and dp[i+1][j-1] if j > i + 1
Time: O(n^2)
Space: O(n^2)
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) and ((i - j < 2) or dp[j + 1][i - 1])
                if dp[j][i]:
                    count += 1
            dp[i][i] = 1
            count += 1
        return count