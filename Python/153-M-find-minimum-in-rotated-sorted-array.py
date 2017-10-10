# Time: O(logn)
# Space: O(1)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low < high -1:
            if nums[low] < nums[high]:
                return nums[low]
            mid = (low+high) // 2
            if nums[mid] > nums[low]:
                low = mid
            else:
                high = mid
        return  min(nums[low],nums[high])

run = Solution()
print(run.findMin([3,1,2]))