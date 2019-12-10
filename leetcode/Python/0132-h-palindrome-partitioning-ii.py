"""
DP
* p[i][j] is a bool indicating whether string[i] to string[j] is a palindrome
* dp[i] is the number of palindromes from string[i] to the last character of the 
  string on the condition of the minimum cuts
Time: O(n^2)
Space: O(n^2)
"""
class Solution:
    def minCut(self, s: str) -> int:
        # initialization
        n = len(s)
        dp = [0 for i in range(n + 1)]
        p = [[False for i in range(n)] for j in range(n)]
        for i in range(n + 1):
            dp[i] = n - i
        # loop over the string in the reverse order from index n - 1 to 0
        for i in range(n - 1, -1, -1):
            # loop over the string from index i to n - 1 (candidate)
            for j in range(i, n):
                # s[i] == s[j]: same character at the two ends of the candidate
                # j - i < 2: the candidate has only one or two characters
                # p[i + 1][j - 1] == True: the inner string of the candidate is a palindrome
                if s[i] == s[j] and ((j - i < 2) or p[i + 1][j - 1]):
                    # string[i] to string[j] is a palindrome
                    p[i][j] = True
                    # pick a min between dp[i] itself and the number of palindromes if cutting at j
                    # the number of palindromes if cutting at j equals 1 + dp[j + 1]
                    dp[i] = min(1 + dp[j + 1], dp[i])
        # return the number of cuts which equals to the number of palindromes  - 1
        return dp[0] - 1
