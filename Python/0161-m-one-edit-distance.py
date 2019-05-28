"""
1. lenDiff > 1, oneEditDist > 1
2. lenDiff = 0, determine if the number of different chars equals one
3. lenDiff = 1, remove the first different char from the longer string 
   and determine if the rests are equal
"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        diff = abs(len(s) - len(t))

        if diff > 1 or s == t:
            return False
        
        if diff == 0:
            cntDiff = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    cntDiff += 1
            return cntDiff == 1
        
        if len(s) > len(t):
            s, t = t, s
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return s[i:] == t[i+1:]
        
        return True
