"""
Binary Search
Time: O(logn)
Space: O(1)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = self.binarySearch(nums, target, "left")
        right = self.binarySearch(nums, target, "right")
        return [left, right]

    def binarySearch(self, nums, target, id):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                if id == "left":
                    end = mid
                else:
                    start = mid
        if id == "left":
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
        else:
            if nums[end] == target:
                return end
            if nums[start] == target:
                return start
        return -1
