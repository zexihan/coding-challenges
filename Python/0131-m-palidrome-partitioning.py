"""
DFS
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.helper(res, [], s, 0)
        return res
    
    def helper(self, res, tempL, s, start):
        if start == len(s):
            res.append(list(tempL))
            return
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                tempL.append(s[start:i + 1])
                self.helper(res, tempL, s, i + 1)
                tempL.pop()
    
    def isPalindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]: 
                return False
            low += 1
            high -= 1
        return True