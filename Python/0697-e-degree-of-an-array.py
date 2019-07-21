"""
Left and Right Index
Time: O(n)
Space: O(n)
"""
import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right = {}, {}
        count = collections.defaultdict(int)
        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i
            count[nums[i]] += 1
        
        res = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                res = min(res, right[x] - left[x] + 1)
        
        return res