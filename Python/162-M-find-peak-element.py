# Time: O(logn)
"""
If num[i-1] < num[i] > num[i+1], then num[i] is peak
If num[i-1] < num[i] < num[i+1], then num[i+1...n-1] must contains a peak
If num[i-1] > num[i] > num[i+1], then num[0...i-1] must contains a peak
If num[i-1] > num[i] < num[i+1], then both sides have peak
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0 , len(nums)-1)

    def helper(self, nums, start, end):
        if start == end:
            return start
        elif start + 1 == end:
            if nums[start] > nums[end]: return start
            return end
        else:
            m = (start + end) / 2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m-1] > nums[m] and nums[m] > nums[m+1]:
                return self.helper(nums, start, m-1)
            else:
                return self.helper(nums, m+1, end)