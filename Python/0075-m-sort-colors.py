"""
Counting Sort with Hash Table
Time: O(n)
Space: O(1)
"""
class Solution_1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        map = {0:0, 1:0, 2:0}
        for n in nums:
            map[n] += 1

        for i in range(len(nums)):
            if i < map[0]:
                nums[i] = 0
            if map[0] <= i < map[0] + map[1]:
                nums[i] = 1
            if i >= map[0] + map[1]:
                nums[i] = 2

"""
Two Pointers
0 pl 1 pr 2
Time: O(n)
Space: O(1)
"""
class Solution_2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == []: 
            return
        pl = 0
        pr = len(nums) - 1
        i = 0
        while i <= pr:
            if nums[i] == 2:
                nums[i], nums[pr] = nums[pr], nums[i]
                pr -= 1
            elif nums[i] == 0:
                nums[i], nums[pl] = nums[pl], nums[i]
                pl += 1
                i += 1
            else:
                i += 1