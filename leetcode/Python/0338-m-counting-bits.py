"""
DP
"""
class Solution:
    def countBits(self, num: int) -> List[int]:
        f = [0 for i in range(num + 1)]
        f[0] = 0
        for i in range(1, num+1):
            f[i] = (i & 1) + f[i >> 1]
        return f