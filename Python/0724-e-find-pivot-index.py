"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        curtSum = 0
        for i in range(len(nums)):
            if curtSum == S - curtSum - nums[i]:
                return i
            curtSum += nums[i]
        return -1
