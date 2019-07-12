"""
Time: O(256n)
Space: O(1)
"""
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLen = float('inf')
        minStr = ""
        sourceHash = collections.defaultdict(int)
        targetHash = collections.defaultdict(int)

        for c in t:
            targetHash[c] += 1

        j = 0
        for i in range(len(s)):
            while not self.valid(sourceHash, targetHash) and j < len(s):
                sourceHash[s[j]] += 1
                j += 1
            if self.valid(sourceHash, targetHash):
                if minLen > j - i:
                    minLen = j - i
                    minStr = s[i:j]
            sourceHash[s[i]] -= 1
        return minStr

    def valid(self, sourceHash, targetHash):
        for c in targetHash.keys():
            if targetHash[c] > sourceHash[c]:
                return False
        return True
