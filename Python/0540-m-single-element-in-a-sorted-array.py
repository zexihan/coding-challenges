"""
Binary Search
0 1 2 3 4 5 6
1 1 2 2 3 4 4
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) % 2 == 0:
            return None
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (mid == 0 and nums[mid] != nums[mid+1]) or \
               (mid == len(nums) - 1 and nums[mid] != nums[mid - 1]) or \
               (nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
                return nums[mid]
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or \
               (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                left  = mid + 1
            else:
                right = mid - 1
        return nums[left]
