"""
Sort and use two pointers
Time: O(n^2)
Space: O(1)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minDiff = float('inf')
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                curDiff = abs(curSum - target)
                if curDiff < minDiff:
                    minDiff = curDiff
                    res = curSum
                if curSum > target:
                    right -= 1
                elif curSum < target:
                    left += 1
                else:
                    return target
        return res
