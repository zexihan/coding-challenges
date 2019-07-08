"""
DP
F[1] = 1
F[i] = max{1, F[j]+1 | aj<ai and j < i}
Time: O(n^2)
Space: O(n)
"""
class Solution_1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for curt in range(n):
            for prev in range(curt):
                if nums[curt] > nums[prev]:
                    dp[curt] = max(dp[curt], dp[prev] + 1)
        return max(dp)

"""
Binary Search
Time: O(nlogn)
Space: O(n)
"""
class Solution_2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for x in range(len(nums)):
            start = 0
            end = len(res) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if res[mid] < nums[x]:
                    start = mid + 1
                else:
                    end = mid - 1
            if start >= len(res):
                res.append(nums[x])
            else:                               
                res[start] = nums[x]
        return len(res)
