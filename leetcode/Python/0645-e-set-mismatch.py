"""
Sorting
Time: O(nlogn)
Space: O(1)
"""
class Solution_1:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        missing, dup = 1, -1
        nums.sort()
        for i in range(1, N):
            if nums[i] == nums[i - 1]:
                dup = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                missing = nums[i - 1] + 1
        if N != nums[N - 1]:
            missing = N
        return [dup, missing]

"""
Inversion
Time: O(n)
Space: O(1)
"""
class Solution_2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing, dup = 1, -1
        for n in nums:
            if nums[abs(n) - 1] < 0:
                dup = abs(n)
            else:
                nums[abs(n) - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
        
        return [dup, missing]
