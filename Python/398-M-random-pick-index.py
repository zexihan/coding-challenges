"""
Reservoir Sampling
"""
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res, cnt = None, 0
        for pos, num in enumerate(self.nums):
            if target == num:
                if random.randint(0, cnt) == 0:
                    res = pos
                cnt += 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
