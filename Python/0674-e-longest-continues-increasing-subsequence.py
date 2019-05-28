class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [0 for i in range(n)]
        res = 0
        for i in range(n):
            dp[i] = 1

            if i > 0 and nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1

            res = max(res, dp[i])

        return res
