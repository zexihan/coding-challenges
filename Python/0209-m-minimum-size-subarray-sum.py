# A better brute force
# Time: O(n^2)
# Space: O(n)
class Solution:
    def minSubArrayLen_TLE(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
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

# Using two pointers
# Time: O(n)
# Space: O(1)
class Solution_2:    
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sum = 0
        left = 0
        ans = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                ans = min(ans, i - left + 1)
                sum -= nums[left]
                left += 1
        return int(ans) if ans != float('inf') else 0