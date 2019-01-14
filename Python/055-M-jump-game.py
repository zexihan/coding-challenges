# DP - TLE
# f[j] = OR_{0<=i<j}(f[i] AND i + a[i] >= j)
# f[0] = True
# Time: O(n^2)
# Space: O(n)
class Solution_1:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        f = [False] * n

        # init
        f[0] = True
        for j in range(1, n):
            # previous stone i before j
            # last jump from i to j
            # OR..
            for i in range(j):
                if f[i] and i + nums[i] >= j:
                    f[j] = True
                    break
        
        return f[n - 1]

# Greedy
class Solution_2:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0