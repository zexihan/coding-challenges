"""
Time: O(n)
Space: O(n)
"""
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1
        prefixSum = 0
        res = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum - k in d:
                res += d[prefixSum - k]
            d[prefixSum] += 1
        return res