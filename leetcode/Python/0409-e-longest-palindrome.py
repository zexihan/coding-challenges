"""
Time: O(n)
Space: O(1)
"""
import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        chars = collections.defaultdict(int)
        for c in s:
            chars[c] += 1
        for _, v in chars.items():
            res += v // 2 * 2
            if res % 2 == 0 and v % 2 == 1:
                res += 1
        return res