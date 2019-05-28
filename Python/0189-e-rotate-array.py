class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        return nums

if __name__ == "__main__":
    new = Solution()
    print(new.rotate([1,2,3,4,5,6,7], 3))
    print(new.rotate([1,2], 1))