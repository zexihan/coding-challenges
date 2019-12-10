"""
Modified Merge Sort
left reverse pairs + right reverse pairs + split reverse pairs
Time: O(nlog^2n)
"""
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, start, end):
        if start >= end:
            return 0
        mid = (start + end) // 2
        res = self.helper(nums, start, mid) + self.helper(nums, mid + 1, end)
        nums[start: mid + 1] = sorted(nums[start: mid + 1])
        nums[mid + 1: end + 1] = sorted(nums[mid + 1: end + 1])
        i = start
        j = mid + 1
        while i <= mid and j <= end:
            if nums[i] > 2 * nums[j]:
                res += mid - i + 1
                j += 1
            else:
                i += 1
        return res
