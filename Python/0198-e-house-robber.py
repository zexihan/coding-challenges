# Time: O(n)
# Space: O(1)
"""
Dynamic Programming
Induction rule: max[i + 1] = max(max[i], max[i - 1] + money[i]) # Space: O(n)
-> next = max(cur, prev + money[i]) # Space: O(1)
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

        prev = 0
        cur = nums[0]

        for i in range(1, len(nums)):
            next = max(cur, nums[i] + prev)
            prev = cur
            cur = next
        
        return cur

if __name__ == "__main__":
    new = Solution()
    print(new.rob([1, 4, 4, 9, 0, 1, 3, 2])) # 16
