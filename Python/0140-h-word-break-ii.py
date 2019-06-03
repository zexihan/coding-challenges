"""
Recursion with memoization
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.breakW(s, {}, set(wordDict))
    
    def breakW(self, s, mem, words):
        if s in mem:
            return mem[s]
        res = []
        if s in words:
            res.append(s)
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            if right not in words:
                continue
            res += [w + " " + right for w in self.breakW(left, mem, words)]
        mem[s] = res
        return mem[s]
