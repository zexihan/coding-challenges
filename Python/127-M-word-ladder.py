# bfs
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = collections.deque()
        q.append((beginWord, 1))
        wordSet = set(wordList)
        while q:
            word, lens = q.popleft()
            if word == endWord:
                return lens
            for i in range(len(word)):
                for c in 'abcdefghigklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet and newWord != word:
                        q.append((newWord, lens + 1))
                        wordSet.remove(newWord)
        return 0

if __name__ == "__main__":
    print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
