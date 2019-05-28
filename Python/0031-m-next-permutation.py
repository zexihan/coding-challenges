"""
1. 在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
2. 然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换。
3. 然后将partition后的元素（不包括partition指向的元素）逆序排列。
e.g. 14532
1. 那么升序对为45，partition指向4。
2. 由于partition之后除了5没有比4大的数，所以45交换为54，即15432。
3. 然后将partition之后的元素逆序排列，即432排列为234，则最后输出的next permutation为15234。
"""
# Time: O(n)
# Space: O(1)
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i + 1)

    def reverse(self, nums, start):
        i, j= start, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1