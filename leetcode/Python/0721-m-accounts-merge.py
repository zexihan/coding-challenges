"""
Union Find
Time: O(AlogA) where A = sum(ai), and ai is the length of accounts[i]
Space: O(A)
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.parent = list(range(10001))
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                self.union(em_to_id[acc[1]], em_to_id[email])
        res = collections.defaultdict(list)
        for email in em_to_name:
            res[self.find_parent(em_to_id[email])].append(email)
        return [[em_to_name[v[0]]] + sorted(v) for v in res.values()]

    def find_parent(self, i):
        path = []
        while self.parent[i] != i:
            path.append(i)
            i = self.parent[i]
        for p in path:
            self.parent[i] = i
        return i

    def union(self, x, y):
        x_set = self.find_parent(x)
        y_set = self.find_parent(y)
        if x_set != y_set:
            self.parent[y_set] = x_set
