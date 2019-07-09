"""
2 * 2Sum
Time: O(n^2)
Space: O(n)
"""
import collections
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dic = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum2 = nums[i] + nums[j]
                dic[sum2].append((i, j))
        
        res = set()
        for key in dic:
            val = target - key
            if val in dic:
                list1 = dic[key]
                list2 = dic[val]
                for (i, j) in list1:
                    for (k, l) in list2:
                        if i != k and i != l and j != k and j != l:
                            res.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
        return list(res)
