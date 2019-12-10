"""
Brute Force
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

class Solution_1:
    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s, p, 0, 0)

    def helper(self, s, p, i, j):
        if j == len(p):
            return i == len(s)
        # case1: p[j+1] != "*"
        if j == len(p) - 1 or p[j+1] != "*":
            if i == len(s) or s[i] != p[j] and p[j] != ".":
                return False
            else:
                return self.helper(s, p, i+1, j+1)
        # case2: p[j+1] == "*"
        # check s[i],s[i+1],...s[i+k] equal or not equal to p[j]
        while i < len(s) and (p[j] == "." or s[i] == p[j]):
            # check (i,j+2),(i+1,j+2),...,(i+k,j+2)
            if self.helper(s, p, i, j+2):
                return True
            i += 1
        # jump over the current and the "*"
        return self.helper(s, p, i, j+2) 


"""
DP
1. If p[j] == s.[i] :  dp[i][j] = dp[i-1][j-1];
2. If p[j] == '.' : dp[i][j] = dp[i-1][j-1];
3. If p[j] == '*': 
   here are two sub conditions:
               a. if p[j-1] != s[i] : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
               b. if p[j-1] == s[i] or p[i-1] == '.':
                            dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
                        or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
                        or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
"""
class Solution_2:
    def isMatch(self, s: str, p: str) -> bool:
        if not s or not p:
            return False
        dp = [[False] * (len(p) + 1)] * (len(s) + 1)
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] == "*":
                if dp[0][j-1] or (j > 1 and dp[0][j-2]):
                    dp[0][j] = True
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == "." or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == "*":
                    if p[j-2] != s[i-1] and p[j-2] != ".":
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i][j-2]
        return dp[len(s)][len(p)]