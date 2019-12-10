class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n==0:
            return 0
        
        res = 0
        for i in range(32):
            res = res<<1
            res += n & 1 # last bit
            n = n >> 1
        return res