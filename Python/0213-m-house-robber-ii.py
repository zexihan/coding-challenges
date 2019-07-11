"""
Dynamic Programming
all cases {
    rob 0 -> max == 7
    rob 4(last) -> max == 9
} find max
Time: O(n)
Space: O(1)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(self.subRob(nums, 0, len(nums) - 2), self.subRob(nums, 1, len(nums) - 1))

    def subRob(self, nums, start, end):
        prev = 0
        cur = nums[start]

        for i in range(start + 1, end + 1):
            next = max(cur, prev + nums[i])
            prev = cur
            cur = next
        
        return cur
