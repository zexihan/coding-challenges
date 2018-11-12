# Time: O(n)
# Space: O(n)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
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