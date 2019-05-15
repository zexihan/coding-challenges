"""
dfs + pruning
"""
import collections
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        m = len(words)
        n = len(words[0]) if m else 0
        prefixDict = collections.defaultdict(set)
        for word in words:
            for i in range(n):
                prefixDict[word[:i]].add(word)
        matrix = []
        res = []
        for word in words:
            self.dfs(word, 1, n, matrix, res, prefixDict)
        return res
    
    def dfs(self, word, line, n, matrix, res, prefixDict):
        matrix.append(word)
        if line == n:
            res.append(matrix[:])
        else:
            prefix = ''.join(matrix[x][line] for x in range(line))
            for word in prefixDict[prefix]:
                self.dfs(word, line + 1, n, matrix, res, prefixDict)
        matrix.pop()
