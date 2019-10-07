"""
Two Pointers
Time: O(n * xlogn + n * x)
Space: O(logn)
"""
class Solution_1:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        for w in sorted(d, key = lambda x: (-len(x), x)):
            if self.isMatch(s, w):
                return w
        return ""

    def isMatch(self, s, w):
        i, j = 0, 0
        while i < len(s):
            if s[i] == w[j]:
                j += 1
                if j == len(w):
                    return True
            i += 1
        return False


class Solution_2:
    def findLongestWord(self, s, d):
        for x in sorted(d, key = lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in x):
                return x
        return ""