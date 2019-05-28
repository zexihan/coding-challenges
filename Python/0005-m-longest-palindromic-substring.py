# Time: O(n^2)
# Space: O(1)
# Center expansion
class Solution_1:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lo, maxLen= 0, 0
        if len(s) < 2:
            return s

        for i in range(len(s)):
            lo, maxLen = self.extendPalindrome(s, i, i, lo, maxLen) # assume odd length
            lo, maxLen = self.extendPalindrome(s, i, i+1, lo, maxLen) # assume even length
        return s[lo:lo + maxLen]

    def extendPalindrome(self, s, j, k, lo, maxLen):
        while j>=0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        if maxLen < k - j - 1:
            lo = j + 1
            maxLen = k - j -1
        return lo, maxLen

'''
DP
dp[i][j] = 1 if i == j
dp[i][j] = s[i] == s[j] if j = i + 1
dp[i][j] = s[i] == s[j] and dp[i+1][j-1] if j > i + 1
Time: O(n^2)
Space: O(n^2)
'''
class Solution_2:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(set(s)) == 1:
            return s
        n = len(s)
        start, end, maxL = 0, 0, 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) & ((i - j < 2) | dp[j + 1][i - 1])
                if dp[j][i] and maxL < i - j + 1:
                    maxL = i - j + 1
                    start = j
                    end = i
            dp[i][i] = 1
        return s[start: end + 1]

if __name__ == "__main__":
    new = Solution_1()
    print(new.longestPalindrome("cbbd"))
    print(new.longestPalindrome("babad"))
    
