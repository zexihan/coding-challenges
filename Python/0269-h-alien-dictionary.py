"""
topological sort, bfs
Time: O(n^2)
Space: O(n*k)
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegrees = {}
        graph = {}
        res = ""
        for word in words:
            for c in word:
                indegrees[c] = 0
                graph[c] = []
        # build graph
        for i in range(1, len(words)):
            k = 0
            length = min(len(words[i-1]), len(words[i]))
            while k < length and words[i-1][k] == words[i][k]:
                k += 1
            if k != length:
                indegrees[words[i][k]] += 1
                graph[words[i-1][k]].append(words[i][k])
        # topological sort
        for i in range(len(indegrees)):
            zeroIndegree = False
            for c in indegrees:
                if indegrees[c] == 0:
                    zeroIndegree = True
                    break
            if not zeroIndegree:
                return ""
            res += c
            indegrees[c] -= 1
            for followingNode in graph[c]:
                indegrees[followingNode] -= 1
        return res
