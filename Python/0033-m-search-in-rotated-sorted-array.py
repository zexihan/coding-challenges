"""
Binary search
Key: Go left or right?

Step1: which part is mid in?
Target in Part 1 or Part 2
    nums[mid] > nums[start] -> nums[mid] in Part 1
    nums[mid] < nums[start] -> nums[mid] in Part 2

Step 2: which part may target be in?
    target >= nums[start] and target < nums[mid] -> target in Part 1
    target < nums[end] and target > nums[mid] -> target in Part 2

Time: O(logn)
Space: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            # locate nums[mid]
            if nums[mid] >= nums[start]:
                # locate target
                if nums[mid] >= target and nums[start] <= target:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target and nums[end] >= target:
                    start = mid
                else:
                    end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
