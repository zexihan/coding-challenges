# Time: O(n^2)
# Space: O(1)
# Center expansion
class Solution(object):
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


if __name__ == "__main__":
    new = Solution()
    print(new.longestPalindrome("cbbd"))
    print(new.longestPalindrome("babad"))
    