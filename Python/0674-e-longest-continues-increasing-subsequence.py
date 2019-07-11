"""
DP
Time: O(n)
Space: O(1)
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        prev = 1
        res = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
               curt = prev + 1
            else:
                curt = 1
            res = max(res, curt)
            prev = curt
        return res
