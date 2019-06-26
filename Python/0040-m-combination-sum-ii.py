"""
DFS
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(sorted(candidates), [], target, 0, res)
        return res
    
    def backtrack(self, candidates, tempL, remain, start, res):
        if remain == 0:
            res.append(tempL[:])
            return
        if remain < 0: 
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]: 
                continue
            tempL.append(candidates[i])
            self.backtrack(candidates, tempL, remain - candidates[i], i + 1, res)
            tempL.pop()
