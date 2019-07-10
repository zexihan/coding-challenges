"""
从 end 到 start 做一次 BFS，并且把距离 end 的距离都保存在 distance 中。
然后在从 start 到 end 做一次 DFS，每走一步必须确保离 end 的 distance 越来越近。

这里寻找下一个变换单词的方法是建立 index，即，如果有一个单词 abc，分别去掉第1,2,3个字符之后，
把 abc 这个单词分别扔进%bc, a%c, ab% 这三个不同的 key 的 hash 里。hash 里的 key 是去掉一
个字符之后的 pattern，value 是一个 set，保存满足这个 pattern 的所有单词。
"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        wordList.add(beginWord)
        distance = {}

        self.bfs(endWord, beginWord, distance, wordList)

        results = []
        self.dfs(beginWord, endWord, distance, wordList, [beginWord], results)

        return results

    def bfs(self, start, end, distance, wordList):
        distance[start] = 0
        queue = collections.deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, wordList):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def get_next_words(self, word, wordList):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in wordList:
                    words.append(next_word)
        return words

    def dfs(self, curt, target, distance, wordList, path, results):
        if curt == target:
            results.append(list(path))
            return

        for word in self.get_next_words(curt, wordList):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, wordList, path, results)
            path.pop()
