# Time:
# Space:
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        if len(nums) == 0: 
            return 0 
        index = 0 
        for i in nums[1:]: 
            if i != nums[index]: 
                index += 1 
                nums[index] = i
        return index + 1