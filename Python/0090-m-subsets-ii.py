
"""
if nums[i] is same to nums[i - 1], then it needn't to be added to all of the subset, 
just add it to the last l subsets which are created by adding nums[i - 1]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums = sorted(nums)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res