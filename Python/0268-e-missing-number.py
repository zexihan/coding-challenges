# Array, Math, Bit Manipulation

class Solution_1:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for num in nums:
            sum += num
        n = len(nums)
        return (n * (n + 1)) // 2 - sum

class Solution_2:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for i in range(len(nums)):
            xor ^= i ^ nums[i]
        return xor ^ len(nums)