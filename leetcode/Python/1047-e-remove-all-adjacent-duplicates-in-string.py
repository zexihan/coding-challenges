"""
Stack
Time: O(n)
Space: O(n)
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        resList = []
        for ch in S:
            if resList and ch == resList[-1]:
                resList.pop()
            else:
                resList.append(ch)
        return ''.join(resList)