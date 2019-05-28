"""
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        cntS = [0] * 256
        cntT = [0] * 256
        for c in s:
            cntS[ord(c)] += 1
        for c in t:
            cntT[ord(c)] += 1
        return cntS == cntT
