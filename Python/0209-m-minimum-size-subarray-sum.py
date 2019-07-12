"""
A better brute force
Time: O(n^2)
Space: O(n)
"""
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(sums[i-1] + nums[i])
        ans = float("inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = sums[j] - sums[i] + nums[i]
                if sum >= s:
                    ans = min(ans, j - i + 1)
        return int(ans) if ans != float("inf") else 0

"""
Using two pointers
Time: O(n)
Space: O(1)
"""
class Solution_2:    
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        curtSum = 0
        res = float('inf')
        for i in range(n):
            while j < n and curtSum < s:
                curtSum += nums[j]
                j += 1

            if curtSum >= s:
                res = min(res, j - i)

            curtSum -= nums[i]
        return res if res != float('inf') else 0
