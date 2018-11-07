class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_dist = float('Inf')
        nums = sorted(nums)
        cur = 0
        while cur < len(nums) - 2:
            nex, las = cur + 1, len(nums) - 1
            while nex < las:
                cur_sum = nums[cur] + nums[nex] + nums[las]
                cur_dist = abs(cur_sum - target)
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    result = cur_sum
                if cur_sum > target:
                    las -= 1
                elif cur_sum < target:
                    nex += 1
                else:
                    return target
            cur += 1
        return result