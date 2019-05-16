"""
dfs
Time: O(VlogV)
Space: O(E)
首先肯定是要把路径保存成链表法表示的图的。然后对每个顶点的所有邻接顶点进行排序，
这样我们每次都优先选择字典序最小的那个顶点作为下次遍历的节点。我们做了后序遍历即
可。最后还要把后序遍历的结果再翻转，才是从根节点出发到每个位置的路径。
"""
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
        for frm, tos in graph.items():
            tos.sort(reverse = True)
        res = []
        self.dfs(graph, "JFK", res)
        return res[::-1]
    
    def dfs(self, graph, src, res):
        while graph[src]:
            v = graph[src].pop()
            self.dfs(graph, v, res)
        res.append(src)
