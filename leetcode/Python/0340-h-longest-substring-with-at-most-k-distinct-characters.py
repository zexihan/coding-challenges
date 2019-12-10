"""
Time: O(n)
Space: O(1)
"""
import collections
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cHash = collections.defaultdict(int)
        j = 0
        maxLen = 0
        for i in range(len(s)):
            while len(cHash) <= k and j < len(s):
                cHash[s[j]] += 1
                j += 1
                if len(cHash) <= k:
                    maxLen = max(maxLen, j - i)
            cHash[s[i]] -= 1
            if cHash[s[i]] == 0:
                del cHash[s[i]]
        return maxLen
