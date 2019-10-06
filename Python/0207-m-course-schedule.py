"""
https://blog.csdn.net/fuxuemingzhu/article/details/82951771
Topological sort, BFS
Time: O(n^2)
Space: O(n)
"""
import collections
class Solution_1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for course, req in prerequisites:
            graph[req].append(course)
            indegrees[course] += 1
        for i in range(numCourses):
            zeroDegree = False
            for j in range(numCourses):
                if indegrees[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree:
                return False
            indegrees[j] -= 1
            for node in graph[j]:
                indegrees[node] -= 1
        return True

"""
Topological sort, DFS
Time: O(n)
Space: O(n)
"""
class Solution_2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for course, req in prerequisites:
            graph[course].append(req)
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    # Can we add node i to visited successfully?
    def dfs(self, graph, visited, i):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 2
        return True

"""
backtracking to see if a course is its own ancestor
edges: dict storing pairs
path: set storing learing (prereq) path for a course
cleared: set storing all cleared prereq
"""
class Solution_3:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        edges = {}
        for course, req in prerequisites:
            if course not in edges:
                edges[course] = [req]
            else:
                edges[course].append(req)
        
        def helper(path, course):
            for req in edges[course]:
                if req in path:
                    return False
                if req in edges and req not in cleared:
                    path.add(req)
                    flag = helper(path, req)
                    path.remove(req)
                    if not flag:
                        return False
                    else:
                        cleared.add(req)
            return True
        
        cleared = set()
        for course in edges.keys():
            if not helper(set(), course):
                return False
        return True