class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        insertPos = 0
        for num in nums:
            if num != 0:
                nums[insertPos] = num
                insertPos += 1
        while insertPos < len(nums):
            nums[insertPos] = 0
            insertPos += 1
        
        return  nums

if __name__ == "__main__":
    new = Solution()
    print(new.moveZeroes([0, 1, 0, 3, 12]))