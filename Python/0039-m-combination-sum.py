"""
DFS
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(sorted(candidates), [], target, 0, res)
        return res

    def dfs(self, candidates, sublist, target, last, res):
        if target == 0:
            res.append(sublist[:])
        if target < candidates[0]:
            return
        for n in candidates:
            if n > target:
                return
            if n < last:
                continue
            sublist.append(n)
            self.dfs(candidates, sublist, target - n, n, res)
            sublist.pop()

if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 6, 7], 7))
