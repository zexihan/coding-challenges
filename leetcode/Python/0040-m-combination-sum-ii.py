"""
DFS
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(sorted(candidates), [], 0, target, res)
        return res

    def helper(self, candidates, path, start, target, res):
        if target == 0:
            res.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.helper(candidates, path, i + 1, target - candidates[i], res)
            path.pop()
