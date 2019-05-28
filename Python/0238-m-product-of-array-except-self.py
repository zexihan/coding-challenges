# Time: O(n)
# Space: O(1)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        res[0] = 1
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(n-1,-1,-1):
            res[i] *= right
            right *= nums[i] 
        return res

if __name__ == "__main__":
    new = Solution()
    print(new.productExceptSelf([1,2,3,4])) # [24,12,8,6]