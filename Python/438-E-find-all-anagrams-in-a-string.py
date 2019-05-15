import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        m, n = len(s), len(p)
        if m < n:
            return res
        pCounter = collections.defaultdict(int)
        for c in p:
            pCounter[c] += 1
        sCounter = collections.defaultdict(int)
        for c in s[:n-1]:
            sCounter[c] += 1
        for i in range(n - 1, m):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                res.append(i - n + 1)
            sCounter[s[i - n + 1]] -= 1
            if sCounter[s[i - n + 1]] == 0:
                del sCounter[s[i - n + 1]]
        return res

