"""
set, bit
a^b = c, 则有 a^c = b，且 b^c = a
https://kingsfish.github.io/2017/12/15/Leetcode-421-Maximum-XOR-of-Two-Numbers-in-an-Array/
"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = mask = 0
        for x in range(31, -1, -1):
            mask += 1 << x
            prefixSet = set([n & mask for n in nums])
            temp = res | 1 << x
            for prefix in prefixSet:
                if temp ^ prefix in prefixSet:
                    res = temp
                    break
        return res
