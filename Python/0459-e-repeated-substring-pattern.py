"""
String
Time: O(kn)
Space: O(1)
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                sub = s[:i]
                if sub * (len(s) // i) == s:
                    return True
        return False
