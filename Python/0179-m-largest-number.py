from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))              
        nums.sort(key=cmp_to_key(lambda x, y: int(x+y) - int(y+x)), reverse=True)                
        return ''.join(nums if nums[0] != '0' else '0')