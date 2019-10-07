"""
Time: O(nlogn)
Space: O(n)
"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums)
        s, t = (len(nums) + 1) // 2, len(nums)
        for i in range(len(nums)):
            if i % 2 == 0:
                s -= 1
                nums[i] = temp[s]
            else:
                t -= 1
                nums[i] = temp[t]
