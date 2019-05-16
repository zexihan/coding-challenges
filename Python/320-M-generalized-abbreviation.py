"""
dfs, backtracking
"""
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        self.dfs(res, word, "")
        return res
    
    def dfs(self, res, word, string):
        if len(word) == 0:
            res.append(string)
            return res
        self.dfs(res, word[1:], string + word[0])
        for i in range(1, len(word)):
            self.dfs(res, word[i+1:], string + str(i) + word[i])
        self.dfs(res, "", string + str(len(word)))
        
