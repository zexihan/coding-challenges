"""
if nums[i] is same to nums[i - 1], then it needn't to be added to all of the subset, 
just add it to the last l subsets which are created by adding nums[i - 1]
"""
class Solution_1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums = sorted(nums)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res

"""
DFS
"""
class Solution_2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, startIndex, path, res):
        res.append(path)
        for i in range(startIndex, len(nums)):
            if i != startIndex and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], res)
