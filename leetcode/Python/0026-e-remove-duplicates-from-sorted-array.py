# Time: O(n)
# Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0 
        index = 0 
        for i in nums[1:]: 
            if i != nums[index]: 
                index += 1 
                nums[index] = i
        return index + 1