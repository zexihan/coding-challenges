# Time:
# Space:
class Solution_1(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
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
                nums[i] =2
        return nums


# Time:
# Space:
class Solution_2(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []: return
        p0 = 0
        p2 = len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            else:
                i += 1
        return nums

if __name__ == '__main__':
    new_1 = Solution_1()
    new_2 = Solution_2()
    print(new_1.sortColors([2, 0, 1, 0, 2, 1, 1, 0, 2]))
    print(new_2.sortColors([2, 0, 1, 0, 2, 1, 1, 0, 2]))