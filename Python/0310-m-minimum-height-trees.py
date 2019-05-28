"""
topological sort, bfs
把所有的叶子节点放入队列中，然后同时向中间遍历，这样最后剩下来的就是整棵树中间的元素，可以是1个或者2个。
Time: O(|V|)
Space: O(|E| + |V|)
"""
import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        leaves = collections.defaultdict(set)
        for u, v in edges:
            leaves[u].add(v)
            leaves[v].add(u)
        
        q = collections.deque()
        for u, vs in leaves.items():
            if len(vs) == 1:
                q.append(u)
        
        while n > 2:
            n -= len(q)
            for _ in range(len(q)):
                u = q.popleft()
                for v in leaves[u]:
                    leaves[v].remove(u)
                    if len(leaves[v]) == 1:
                        q.append(v)
        
        return list(q)
