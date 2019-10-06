"""
DP
dp[i] represents the number of decode ways with the first i characters of the string
1. dp[i] = dp[i-1] + dp[i-2], 10<=s[i-2:i]<=26 and s[i-2:i] != [10 or 20]
2. dp[i] = dp[i-2], s[i-2:i] = [10 or 20]
3. dp[i] = dp[i-1], others
Init: dp[0]=1, dp[1]=1
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == "0":
            return 0
        
        dp = [1,1]
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i - 2 : i]) <= 26 and s[i - 1] != "0":
                dp.append(dp[i - 1] + dp[i - 2])
            elif int(s[i - 2 : i]) == 10 or int(s[i - 2 : i]) == 20:
                dp.append(dp[i - 2])
            elif s[i - 1] != "0":
                dp.append(dp[i - 1])
            else: return 0
        
        return dp[len(s)]