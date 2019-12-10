"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for z in zip(*strs):
            bag = set(z)
            if len(bag) == 1:
                prefix += bag.pop()
            else:
                break
        return prefix
