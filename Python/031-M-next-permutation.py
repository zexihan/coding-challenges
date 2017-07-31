"""
1. 在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
2. 然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换。
3. 然后将partition后的元素（不包括partition指向的元素）逆序排列。
e.g. 14532
1. 那么升序对为45，partition指向4。
2. 由于partition之后除了5没有比4大的数，所以45交换为54，即15432。
3. 然后将partition之后的元素逆序排列，即432排列为234，则最后输出的next permutation为15234。
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            partition = -1
            # step 1
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    partition = i
                    break
            # step 2 & 3
            if partition == -1:
                nums.reverse()
            else:
                for i in range(len(nums) - 1, partition, -1):
                    if nums[i] > nums[partition]:
                        nums[i], nums[partition] = nums[partition], nums[i]
                        break
                nums[partition + 1 : len (nums)] = nums[partition + 1 : len(nums)][::-1]
