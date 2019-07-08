"""
DP
Time: O(n^2) - TLE
Space: O(n)
"""
class Solution_1:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # init
        f = [False] * n
        f[0] = True

        # function
        for curt in range(1, n):
            for prev in range(curt):
                if f[prev] and prev + nums[prev] >= curt:
                    f[curt] = True
                    break
        # answer
        return f[n - 1]

"""
Greedy
"""
class Solution_2:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0
