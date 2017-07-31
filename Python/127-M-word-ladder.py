# start from beginWord
from collections import deque
import string as str
class Solution_1(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not (beginWord and endWord and wordList):
            return 0
        return self.bfsHelper(beginWord, endWord, wordList)

    def bfsHelper(self, beginWord, endWord, wordList):
        queue = deque()
        visited = set()
        steps = 0

        queue.append(beginWord)
        visited.add(beginWord)
        
        while queue:
            size = len(queue)
            steps += 1
            for i in range(size):
                curStr = queue.popleft()
                # find a candidate for next level
                for j in range(len(curStr)):
                    for k in list(str.ascii_lowercase[:26]):
                        toStr = self.replace(curStr, j, k)
                        # check result first
                        if toStr == endWord:
                            steps += 1
                            return steps
                        # add to visited set and queue if it is in wordList and not in visited
                        if toStr not in visited and toStr in wordList:
                            visited.add(toStr)
                            queue.append(toStr)
        return 0

    # find next string by replacing char
    def replace(self, curStr, j, k):
        chs = list(curStr)
        chs[j] = k
        return ''.join(chs)

# start from both beginWord and endWord
class Solution_2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not (beginWord and endWord and wordList):
            return 0
        if endWord not in wordList:
            return 0
        return self.bfsHelper(beginWord, endWord, wordList)

    def bfsHelper(self, beginWord, endWord, wordList):
        steps = 0
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)

        beginSet = set()
        endSet = set()
        beginSet.add(beginWord)
        endSet.add(endWord)

        while beginSet and endSet:
            steps += 1
            # always start from a smaller one
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            nextLevel = set()
            for curStr in beginSet:
                for i in range(len(curStr)):
                    for j in list(str.ascii_lowercase[:26]):
                        toCheck = self.replace(curStr, i, j)

                        if toCheck in endSet:
                            return steps + 1

                        if toCheck in wordList and toCheck not in visited:
                            visited.add(toCheck)
                            nextLevel.add(toCheck)
            beginSet = nextLevel
        return 0

    def replace(self, curStr, j, k):
        chs = list(curStr)
        chs[j] = k
        return ''.join(chs)

# pythonic
class Solution_3(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        q = [(beginWord,1)]
        while q:
            e,lens = q.pop(0)
            if e == endWord: return lens
            for i in range(len(e)):
                left = e[:i]
                right = e[i + 1:]
                for c in 'abcdefghigklmnopqrstuvwxyz':
                    if e[i] != c:
                        nextWord = left + c + right
                        if nextWord in wordList:
                            q.append((nextWord,lens + 1))
                            wordList.remove(nextWord)
        return 0


if __name__ == "__main__":
    new_1 = Solution_1()
    new_2 = Solution_2()
    new_3 = Solution_3()
    print(new_1.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # 5
    print(new_2.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # 5
    print(new_3.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # 5