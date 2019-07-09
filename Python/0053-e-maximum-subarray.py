"""
Prefix sum
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        minSum = 0
        res = float('-inf')
        for i in range(len(nums)):
            sum += nums[i]
            res = max(res, sum - minSum)
            minSum = min(minSum, sum)
        return res