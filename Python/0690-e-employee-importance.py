"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

"""
BFS
Time: O(n)
Space: O(n)
"""
import collections
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        importances = {}
        for e in employees:
            importances[e.id] = e.importance
            for sId in e.subordinates:
                graph[e.id].append(sId)

        res = 0
        q = collections.deque([id])
        while q:
            eId = q.popleft()
            res += importances[eId]
            for sId in graph[eId]:
                q.append(sId)
        return res
