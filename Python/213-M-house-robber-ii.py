# Time:
# Space:
"""
Dynamic Programming
all cases {
    rob 0 -> max == 7
    rob 4(last) -> max == 9
} find max
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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

if __name__ == "__main__":
    new = Solution()
    print(new.rob([1, 4, 4, 3, 5])) # 9