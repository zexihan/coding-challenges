class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        l = []
        self.backtrack(l, [], s, 0)
        return l
    
    def backtrack(self, l, tempL, s, start):
        if start == len(s):
            l.append(list(tempL))
        else:
            for i in range(start, len(s)):
                if self.isPalindrome(s, start, i):
                    tempL.append(s[start:i + 1])
                    self.backtrack(l, tempL, s, i + 1)
                    tempL.pop()
    
    def isPalindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]: return False
            low += 1
            high -= 1
        return True