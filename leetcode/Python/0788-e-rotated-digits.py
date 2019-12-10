"""
Brute Force
Time: O(Nlog(10)N)
space: O(1)
"""
class Solution_1:
    def rotatedDigits(self, N: int) -> int:
        res = 0
        s1 = set(['3', '4', '7'])
        s2 = set(['2', '5', '6', '9'])
        for x in range(1, N + 1):
            S = str(x)
            if all(d not in s1 for d in S) and any(d in s2 for d in S):
                res += 1
        return res

"""
DP
dp[i] = 0, invalid number
dp[i] = 1, valid and same number
dp[i] = 2, valid and different number

dp[i] = 1 dp[i / 10] == 1 and dp[i % 10] == 1
        2 (dp[i // 10] == 1 and dp[i % 10] == 2) or 
          (dp[i // 10] == 2 and dp[i % 10] == 1) or
          (dp[i // 10] == 2 and dp[i % 10] == 2)
        0 other

Time: O(logN)
Space: O(N)
"""
class Solution_2:
    def rotatedDigits(self, N: int) -> int:
        dp = [0 for i in range(N + 1)]
        res = 0
        for i in range(0, N + 1):
            if i < 10:
                if i in [0, 1, 8]:
                    dp[i] = 1
                elif i in [2, 5, 6, 9]:
                    dp[i] = 2
                    res += 1
            else:
                a = dp[i // 10]
                b = dp[i % 10]
                if a == 1 and b == 1:
                    dp[i] = 1
                elif a >= 1 and b >= 1:
                    dp[i] = 2
                    res += 1
        return res
