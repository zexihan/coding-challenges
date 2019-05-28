class Solution_1:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums:
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res

class Solution_2:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = set(nums)
        new = set(range(1, len(nums) + 1))
        return list(new - n)
