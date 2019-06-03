"""
dfs + pruning
two types of redundancy
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
                if not self.checkPrefix(line, n, word, matrix, prefixDict):
                    continue
                self.dfs(word, line + 1, n, matrix, res, prefixDict)
        matrix.pop()

    def checkPrefix(self, line, n, nextWord, matrix, prefixDict):
        for i in range(line + 1, n):
            prefix = ""
            for item in matrix:
                prefix += item[i]
            prefix += nextWord[i]
            if prefix not in prefixDict:
                return False
        return True
