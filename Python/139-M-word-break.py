# DP
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        f = [False] * (len(s) + 1)
        f[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        return f[len(s)]

if __name__ == "__main__":
    new = Solution()
    print(new.wordBreak("leetcode",["leet", "code"]))