"""
Binary Search
Time: O(logn)
Space: O(1)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        target = nums[end]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                end = mid
            else:
                start = mid
        
        if nums[start] <= target:
            return nums[start]
        else:
            return nums[end]