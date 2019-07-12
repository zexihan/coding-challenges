"""
DFS
"""
class Solution_1:
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
DP
0/1 knapsack
"""
class Solution_2:
    def canPartition(self, nums: List[int]) -> bool:
        div, mod = divmod(sum(nums), 2)
        if mod or max(nums) > div:
            return False
        n = len(nums)
        dp = [False] * (div + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(div, -1, -1):
                if i >= num:
                    dp[i] = dp[i] or dp[i - num]
        return dp[div]