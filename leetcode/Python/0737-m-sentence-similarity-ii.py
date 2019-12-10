"""
DFS
Time: O(NP)
Space: O(P)
"""
import collections
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        graph = collections.defaultdict(list)
        for w1, w2 in pairs:
            graph[w1].append(w2)
            graph[w2].append(w1)

        for w1, w2 in zip(words1, words2):
            stack, seen = [w1], {w1}
            while stack:
                word = stack.pop()
                if word == w2:
                    break
                for nei in graph[word]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            else:
                return False
        return True
        
"""
Union Find
Time: O(NlogP + P)
Space: O(P)
"""
class Solution_2:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        self.parent = list(range(2 * len(pairs)))
        index = {}
        count = 0
        for pair in pairs:
            for p in pair:
                if p not in index:
                    index[p] = count
                    count += 1
            self.union(index[pair[0]], index[pair[1]])

        return all(w1 == w2 or
                   w1 in index and w2 in index and
                   self.find(index[w1]) == self.find(index[w2])
                   for w1, w2 in zip(words1, words2))

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

    def find(self, x):
        path = []
        while x != self.parent[x]:
            path.append(x)
            x = self.parent[x]

        for p in path:
            self.parent[p] = x
        return x
