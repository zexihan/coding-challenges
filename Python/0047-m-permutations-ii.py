# Time: O(n!)
# Space: O(n * 2)
# DFS and using a set in each pos to remove duplicates
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfsHelper(nums, 0)
        return self.res

    def dfsHelper(self, nums, pos):
        # base case: filled in all positions
        if pos == len(nums):
            lst = nums
            self.res.append(lst[:])
            return
        
        used = set()
        for i in range(pos, len(nums)):
            if nums[i] not in used:
                used.add(nums[i])
                nums[i], nums[pos] = nums[pos], nums[i]
                self.dfsHelper(nums, pos + 1)
                nums[i], nums[pos] = nums[pos], nums[i]


if __name__ == "__main__":
    new = Solution()
    print(new.permuteUnique([1, 2, 1]))