"""
Recursion with memorization
"""
class Solution_1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.canBreak(s, {}, set(wordDict))
    
    def canBreak(self, s, mem, words):
        if s in mem: 
            return mem[s]
        if s in words:
            mem[s] = True
            return True
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            if right in words and self.canBreak(left, mem, words):
                mem[s] = True
                return True
        mem[s] = False
        return False

"""
DP
  0      1 2 3 4 5 6 7 8
s space  l e e t c o d e
f 1      0 0 0 1 0 0 0 1
               j       i
f[i] = True if we can break s[1...i]
f[0] = True
for i = 1 to n
    for j = 0 to i
        f[i] = True if f[j] and s[j+1...i] in wordDict
res = f[n]
Time: O(n^3)
Space: O(n)
"""
class Solution_2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        s = " " + s # s[1...n]
        f = [False] * (n + 1)
        f[0] = True
        for i in range(1, n + 1):
            for j in range(0, i):
                if f[j] and s[j + 1 : i + 1] in wordSet:
                    f[i] = True
                    break
        return f[n]

if __name__ == "__main__":
    print(Solution_1().wordBreak("leetcode", ["leet", "code"]))
    print(Solution_2().wordBreak("leetcode", ["leet", "code"]))
