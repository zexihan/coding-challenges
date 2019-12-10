"""
DP
f[i][0] = max(f[i-1][1], f[i-1][0])
f[i][1] = f[i-1][0] + num[i-1]
Time: O(n)
Space: O(n)
"""
class Solution_1:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [[0, 0] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i - 1]
        return max(dp[n][0], dp[n][1])

"""
Optimized DP
f[i] = max(f[i - 1], f[i - 2] + nums[i - 1]) # Space: O(n)
-> next = max(cur, prev + money[i]) # Space: O(1)
Time: O(n)
Space: O(1)
"""
class Solution_2:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev = 0
        cur = nums[0]

        for i in range(1, len(nums)):
            next = max(cur, nums[i] + prev)
            prev = cur
            cur = next
        
        return cur