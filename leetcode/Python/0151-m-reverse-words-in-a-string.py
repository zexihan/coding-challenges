"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])