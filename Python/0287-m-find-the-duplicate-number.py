"""
Binary Search
"""
class Solution_1:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right - left) // 2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid :
                    count += 1
            if count > mid :
                right = mid - 1
            else:
                left = mid + 1
        return left

class Solution_2:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while(fast != slow):
            slow = nums[slow]
            fast = nums[fast]
        return slow
