"""
DFS
"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10):
            self.dfs(i, n, res)
        return res
    
    def dfs(self, curt, n, res):
        if curt > n:
            return 
        res.append(curt)
        for i in range(0, 10):
            self.dfs(10 * curt + i, n, res)