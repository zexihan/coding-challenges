"""
DFS
Time: O(n! * n)
Space: O(n)
"""
class Solution_1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        self.helper(nums, [], res)
        return res

    def helper(self, nums, lst, res):
        # base case: filled in all positions
        if len(lst) == len(nums):
            res.append(lst[:])
            return
        
        # main cases: for each elem
        for n in nums:
            # position left == nums left (no duplicates)
            if n not in lst:
                lst.append(n)
                # next position
                self.helper(nums, lst, res)
                # empty last position for next iteration
                lst.pop()

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


if __name__ == "__main__":
    print(Solution_1().permute([1, 2, 3]))
    print(Solution_2().permute([1, 2, 3]))
