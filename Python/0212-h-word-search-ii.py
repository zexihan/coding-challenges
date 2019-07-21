import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", set(), res)
        return res
    
    def dfs(self, board, node, i, j, path, visited, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited:
            return
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        node = node.children.get(board[i][j])
        if not node:
            return
        visited.add((i, j))
        for k in range(4):
            self.dfs(board, node, i + dx[k], j +
                     dy[k], path + board[i][j], visited, res)
        visited.remove((i, j))
