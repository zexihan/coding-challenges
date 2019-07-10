"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

"""
BFS
"""
class Solution_1:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        self.bfs(node, dic)
        return nodeCopy
    
    def bfs(self, node, dic):
        q = collections.deque([node])
        while q:
            node = q.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    q.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
"""
DFS
"""
class Solution_2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = Node(neighbor.val, [])
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])
