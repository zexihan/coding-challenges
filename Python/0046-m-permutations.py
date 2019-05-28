# Time: O(n! * n)
# Space: O(n)
# DFS
class Solution_1(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        lst = []
        self.helper(nums, lst)
        return self.res

    def helper(self, nums, lst):
        # base case: filled in all positions
        if len(lst) == len(nums):
            self.res.append(lst[:])
            return
        
        # main cases: for each elem
        for n in nums:
            # position left == nums left (no duplicates)
            if n not in lst:
                lst.append(n)
                # next position
                self.helper(nums, lst)
                # empty last position for next iteration
                lst.pop()


# Swap
class Solution_2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        lst = []
        self.helper(nums, lst, 0)
        return self.res

    def helper(self, nums, lst, pos):
        # base case:
        if pos == len(nums):
            self.res.append(lst[:])
            return
        
        # main cases:
        for i in range(pos, len(nums)):  
            # swap, add/remove pair
            lst.append(nums[i])
            # swap: fix a position for going down
            nums[pos], nums[i] = nums[i], nums[pos]
            self.helper(nums, lst, pos + 1)
            # swap back: free a position for going right
            nums[pos], nums[i] = nums[i], nums[pos]
            lst.pop()

if __name__ == "__main__":
    new_1 = Solution_1()
    new_2 = Solution_2()
    print(new_1.permute([1, 2, 3]))
    print(new_2.permute([1, 2, 3]))