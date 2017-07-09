# Time:
# Space:

# currentSum = currentSum > 0 ? currentSum + arr[i] : arr[i]
# globalMax = currentSum > globalMax ? currentSum : globalMax

class Solution_1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum, globalMax = 0, 0
        for i in range(len(nums)):
            if currentSum > 0:
                currentSum += nums[i]
            else:
                currentSum = nums[i]
            if currentSum > globalMax:
                globalMax = currentSum
        return globalMax

# Time:
# Space:
class Solution_2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = g = -2147483647
        for n in nums:
            l = max(n, l+n)
            g = max(g, l)
        return g


if __name__ == '__main__':
    new_1 = Solution_1()
    new_2 = Solution_2()
    print(new_1.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(new_2.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))