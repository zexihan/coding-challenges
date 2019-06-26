"""
DFS and using a set in each pos to remove duplicates
Time: O(n!)
Space: O(n * 2)
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfsHelper(nums, 0, res)
        return res

    def dfsHelper(self, nums, pos, res):
        # base case: filled in all positions
        if pos == len(nums):
            res.append(nums[:])
            return
        
        used = set()
        for i in range(pos, len(nums)):
            if nums[i] not in used:
                used.add(nums[i])
                nums[i], nums[pos] = nums[pos], nums[i]
                self.dfsHelper(nums, pos + 1, res)
                nums[i], nums[pos] = nums[pos], nums[i]


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 2, 1]))
