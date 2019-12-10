"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        l = 0
        while l < len(nums):
            r = l
            while r + 1 < len(nums) and (nums[r + 1] - nums[r]) == 1:
                r += 1
            if l == r:
                res.append(str(nums[l]))
                l += 1
            else:
                res.append(str(nums[l]) + '->' + str(nums[r]))
                l = r + 1
        return res