"""
DP
Time: O(n^2) - TLE
Space: O(n)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        # init
        steps = [float('inf')] * n
        steps[0] = 0
        
        # function
        for curt in range(n):
            for prev in range(curt):
                if steps[prev] != float('inf') and prev + nums[prev] >= curt:
                    steps[curt] = min(steps[curt], steps[prev] + 1)
        
        # answer
        return steps[n - 1]