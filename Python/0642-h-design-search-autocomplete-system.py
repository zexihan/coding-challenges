"""
Trie
Time: O(k * l)
Space: O(p + q + mlogm)
"""
class TrieNode:
    def __init__(self):
        self.children = dict() # letter: TrieNode
        self.sentences = set() # sentence

import collections
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.buffer = ''
        self.stimes = collections.defaultdict(int)
        self.trie = TrieNode()
        for s, t in zip(sentences, times):
            self.stimes[s] = t
            self.addSentence(s)
        self.tnode = self.trie
    
    def addSentence(self, s):
        node = self.trie
        for letter in s:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
            child.sentences.add(s)

    def input(self, c: str) -> List[str]:
        res = []
        if c != '#':
            self.buffer += c
            if self.tnode: 
                self.tnode = self.tnode.children.get(c)
            if self.tnode: 
                res = sorted(self.tnode.sentences, key = lambda x: (-self.stimes[x], x))[:3]
        else:
            self.stimes[self.buffer] += 1
            self.addSentence(self.buffer)
            self.buffer = ''
            self.tnode = self.trie
        return res
        # Your AutocompleteSystem object will be instantiated and called as such:
        # obj = AutocompleteSystem(sentences, times)
        # param_1 = obj.input(c)
