"""
DFS
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(sorted(candidates), [], target, 0, res)
        return res

    def dfs(self, candidates, sublist, target, start, res):
        if target == 0:
            res.append(sublist[:])
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            sublist.append(candidates[i])
            self.dfs(candidates, sublist, target - candidates[i], i, res)
            sublist.pop()