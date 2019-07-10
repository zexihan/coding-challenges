"""
DFS and using a set in each pos to remove duplicates
Time: O(n!)
Space: O(n * 2)
"""
class Solution_1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        visited = [False] * len(nums)
        self.helper(sorted(nums), [], visited, res)
        return res

    def helper(self, nums, path, visited, res):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if visited[i] or \
                (i != 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                continue
            visited[i] = True
            path.append(nums[i])
            self.helper(nums, path, visited, res)
            path.pop()
            visited[i] = 0


class Solution_2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        self.helper(nums, [], 0, res)
        return res

    def helper(self, nums, lst, pos, res):
        # base case:
        if pos == len(nums):
            res.append(nums[:])
            return

        # main cases:
        for i in range(pos, len(nums)):
            # swap: fix a position for going down
            nums[pos], nums[i] = nums[i], nums[pos]
            self.helper(nums, lst, pos + 1, res)
            # swap back: free a position for going right
            nums[pos], nums[i] = nums[i], nums[pos]
