"""
Loop over bits
Time: O(n)
Space: O(1)
"""
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        mask = 1
        for j in range(0, 32):
            ones = zeros = 0
            for num in nums:
                if num & mask:
                    ones += 1
                else:
                    zeros += 1
            res += ones * zeros
            mask = mask << 1
        return res