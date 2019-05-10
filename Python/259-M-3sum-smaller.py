"""
binary search
Time: O(n^2logn)
Space: O(1)
"""
class Solution_1:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum = 0
        for i in range(len(nums) - 2):
            sum += self.twoSumSmaller(nums, i + 1, target - nums[i])
        return sum
    
    def twoSumSmaller(self, nums, startIndex, target):
        sum = 0
        for i in range(startIndex, len(nums) - 1):
            j = self.binarySearch(nums, i, target - nums[i])
            sum += j - i
        return sum
    
    def binarySearch(self, nums, startIndex, target):
        left = startIndex
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) / 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid - 1
        return left

"""
two pointers
Time: O(n^2)
Space: O(1)
"""
class Solution_2:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum = 0
        for i in range(len(nums) - 2):
            sum += self.twoSumSmaller(nums, i + 1, target - nums[i])
        return sum
    
    def twoSumSmaller(self, nums, startIndex, target):
        sum = 0
        left = startIndex
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                sum += right - left
                left += 1
            else:
                right -= 1
        return sum
