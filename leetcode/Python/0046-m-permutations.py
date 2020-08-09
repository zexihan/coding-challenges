"""
DFS
Time: O(n! * n)
Space: O(n!)
"""
class Solution_1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        self.helper(nums, [], res)
        return res

    def helper(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for n in nums:
            if n in path:
                continue
            path.append(n)
            self.helper(nums, path, res)
            path.pop()

"""
DFS + Swap
"""
class Solution_2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        self.helper(nums, 0, res)
        return res

    def helper(self, nums, pos, res):
        # base case:
        if pos == len(nums):
            res.append(nums[:])
            return

        # main cases:
        for i in range(pos, len(nums)):
            # swap: fix a position for going down
            nums[pos], nums[i] = nums[i], nums[pos]
            self.helper(nums, pos + 1, res)
            # swap back: free a position for going right
            nums[pos], nums[i] = nums[i], nums[pos]
