"""
DFS
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        div, mod = divmod(sum(nums), 2)
        if mod or max(nums) > div:
            return False
        nums.sort(reverse = True)
        return self.dfs(nums, 0, div)
    
    def dfs(self, nums, start, target):
        if target < 0:
            return False
        if target == 0:
            return True
        for i in range(start, len(nums)):
            target -= nums[i]
            if self.dfs(nums, i + 1, target):
                return True
            target += nums[i]
        return False

"""
DP TBD
"""