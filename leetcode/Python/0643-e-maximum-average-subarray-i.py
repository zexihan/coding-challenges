"""
Cumulative Sum
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
        sums = [0] * N
        sums[0] = nums[0]
        for i in range(1, N):
            sums[i] += sums[i - 1] + nums[i]
        res = sums[k - 1] / k
        for i in range(k, len(nums)):
            res = max(res, (sums[i] - sums[i - k]) / k)
        return res

"""
Sliding Window
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
        s = sum(nums[:k])
        res = s
        for i in range(k, N):
            s += nums[i] - nums[i - k]
            res = max(res, s)
        return res / k
